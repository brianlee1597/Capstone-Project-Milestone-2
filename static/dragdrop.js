function loadQuestion() {
  $("#question").html("<b>" + question["question"] + "</b>");
  let choices = question["choice"];
  let answers = question["answer"];
  let shuffled = answers
    .map((value) => ({ value, sort: Math.random() }))
    .sort((a, b) => a.sort - b.sort)
    .map(({ value }) => value);
  for (let i = 1; i < 4; i++) {
    $("#draggable_" + i).html(choices[i - 1]);
    $("#draggable_" + i).attr("data-answer", answers[i - 1]);
    $("#droppable_" + i).html(shuffled[i - 1]);
  }
}

function checkAnswer(draggable, drop) {
  let answer = $(draggable).data("answer");
  console.log("answer : " + answer);
  let choice = $(drop).html();
  console.log("choice: " + choice);
  let selected = "0"
  if (answer == choice) {
    selected = "1"
  }
  $.ajax({
    type: "POST",
    url: "/update_score",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({
      correct: answer === choice,
      plus: 25,
      minus: 15,
      answer: selected,
      quiz_id: quiz_id,
    }),
    success: function (newScore) {
      if (answer === choice) {
        console.log("correct answer");
        $(draggable).hide("fast", "linear");
        $(drop).hide("fast", "linear");
      } else {
        console.log("wrong answer");
        draggable.css("left", 0);
        draggable.css("top", 0);
      }
      $("#score_board").html("Score: " + newScore);
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
}

function nextQuestion() {
  let num_answered = answered.length
  let num_hidden = 0;
  $.each($(".draggable"), function () {
    if ($(this).is(":hidden")) {
      num_hidden++;
    }
  })


  if (num_hidden == 3) {
    num_answered = num_answered + 1
    next_question_id = parseInt(question["id"]) + 1;
    if (next_question_id <= 10) {
      window.location.href = "/quiz/" + next_question_id;
    } else if (num_answered === 10) {
      window.location.href = "/score";
    } else {
      console.log(num_answered)
      console.log(answered)
      alert("Please answer all the questions!");
      window.location.href = "/quiz/all";
    }
  } else {
    alert("You must finish matching all before you can move on!");
  }

  
}

$(document).ready(function () {
  if (answered.includes(quiz_id)) {
    if (answered.length === 10) {
      window.location.href = "/score";
    } else {
      //  would be better to update this to maintain user answers for each question.
      alert("This drag-n-drop question has already been answered!");
      window.location.href = "/quiz/all";
    }
  }

  // need to add different href to the question link so that it first goes through server
  // that way can allow clicking a different href to "submit" even without next button
  for (let i = 1; i <= 10; i++) {
    let question_link = $("<a class='listing'>");
    $(question_link).html(i);
    // $(question_link).attr("href", "/quiz/" + i);
    $(question_link).attr("href", "/update_answered/" + quiz_id + "_" + i);
    $(question_link).css("color", "#aaa");
    if (i == quiz_id) {
      $(question_link).css("font-weight", "400");
      $(question_link).css("font-size", "25px");
      $(question_link).css("color", "#000000");
    }
    $("#questions_nav").append(question_link);
  }

  loadQuestion();

  let count = 0;
  $(".draggable").hover(
    function () {
      $(this).css("background-color", "lightyellow");
      $(this).css("cursor", "move");
    },
    function () {
      $(this).css("background-color", "white");
    }
  );

  $(".draggable").draggable({
    revert: "invalid",
    zIndex: 9999,
    start: function (evt, ui) {
      startPos = ui.helper.position();
    },
  });

  $(".droppable").droppable({
    accept: ".draggable",
    tolerance: "touch",
    classes: {
      "ui-droppable-active": "dragging",
      "ui-droppable-hover": "hovering",
    },
    drop: function (event, ui) {
      count += 1;
      $(ui.draggable).css("zIndex", 10001);

      checkAnswer(ui.draggable, this);

      console.log("Number of tries: " + count.toString());
      $("#number_of_drops").html(
        " You have drag-n-dropped " + count.toString() + " times."
      );
    },
  });

  $("a").click(function (event) {
    let num_hidden = 0;
    $.each($(".draggable"), function () {
      if ($(this).is(":hidden")) {
        num_hidden++;
      }
    });
    if (num_hidden !== 3) {
      event.preventDefault();
      alert("You must finish matching all before you can move on!");
    }
  });

  $("#next_button").click(function (event) {
    nextQuestion();
    event.preventDefault();
  });
});
