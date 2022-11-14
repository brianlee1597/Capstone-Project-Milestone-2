let selected = -1;

function loadQuestion() {
  $("#question").html("<b>" + question["question"] + "</b>");
  for (let i = 0; i < 4; i++) {
    $("#label_" + i).html(question["choice"][i]);
  }
  $("#hint_flower").html(question['hint_flower']);
  $("#hint_content_1").html(question['hint_content_1']);
  $("#hint_content_2").html(question['hint_content_2']);
  $("#flower_picture").attr(
    "src",
    question['img']
  );
}

function checkAnswer(quiz_id, selected) {
  let correct_ans = question["answer"];
  $.ajax({
    type: "POST",
    url: "/update_score",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({
      correct: correct_ans === selected,
      plus: 50,
      minus: 25,
      answer: selected,
      quiz_id: quiz_id,
    }),
    success: function (newScore) {
      if (Number(correct_ans) === Number(selected)) {
        console.log("correct answer");
        $("#selection_box_" + selected).css("background-color", "lightgreen");
      } else {
        console.log("wrong answer");
        $("#hint_box").show("slow");
        $("#selection_box_" + selected).css("background-color", "red");
        $("#selection_box_" + correct_ans).css(
          "background-color",
          "lightgreen"
        );
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

function nextQuestion(selected, answered) {
  let num_answered = answered.length
  if (selected > -1) {
    num_answered = num_answered + 1
  }

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
}

$(document).ready(function () {
  console.log(saved_answers)
  let selected = -1;
  if (answered.includes(quiz_id)) {
    console.log("question has been answered");
    selected = saved_answers[quiz_id];
    let correct_ans = question["answer"];
    console.log("selected : " + selected);
    console.log("correct ans : " + correct_ans);
    if (correct_ans === selected) {
      console.log("correct answer");
      $("#selection_box_" + selected).css("background-color", "lightgreen");
    } else {

      // This question has been answered before
      selected =  saved_answers[quiz_id];

    }
    // if (answered.length === 10) {
    //   window.location.href = "/score";
    // } else {
    //   //  would be better to update this to maintain user answers for each question.
    //   alert("Question has already been answered!");
    //   window.location.href = "/quiz/all";
    // }
  }

  // need to add different href to the question link so that it first goes through server
  // that way can allow clicking a different href to "submit" even without next button
  for (let i = 1; i <= 10; i++) {
    let question_link = $("<a class='listing'>");
    $(question_link).html(i);
    $(question_link).attr("href", "/quiz/" + i);
    //$(question_link).attr("href", "/update_answered/" + quiz_id + "_" + i);
    $(question_link).css("color", "#aaa");
    if (i == quiz_id) {
      $(question_link).css("font-weight", "400");
      $(question_link).css("font-size", "25px");
      $(question_link).css("color", "#000000");
    }
    $("#questions_nav").append(question_link);
  }

  loadQuestion();
  $("#hint_box").hide();

  if (selected > -1) {
    if (question['answer'] == selected) {
      $("#selection_box_" + selected).css("background-color", "lightgreen");
    } else {
      console.log("wrong answer");
      $("#hint_box").show("slow");
      $("#selection_box_" + selected).css("background-color", "red");
      $("#selection_box_" + question['answer']).css(
        "background-color",
        "lightgreen"
      );
    }
  }

  $("#selection_box_0").click(function () {
    if (selected == -1) {
      selected = 0;
      checkAnswer(quiz_id, "0");
    }
  });

  $("#selection_box_1").click(function () {
    if (selected == -1) {
      selected = 1;
      checkAnswer(quiz_id, "1");
    }
  });

  $("#selection_box_2").click(function () {
    if (selected == -1) {
      selected = 2;
      checkAnswer(quiz_id, "2");
    }
  });

  $("#selection_box_3").click(function () {
    if (selected == -1) {
      selected = 3;
      checkAnswer(quiz_id, "3");
    }
  });

  $("#quiz_button").click(function (event) {
    window.location.href = "/quiz/all";
    event.preventDefault();
  });

  $("#next_button").click(function (event) {
    nextQuestion(selected, answered);
    event.preventDefault();
  });
});
