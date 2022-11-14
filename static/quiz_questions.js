function loadQuestions(questions) {
  $("#quiz_questions_listing").empty();

  let row = $("<div class= 'row'>");

  $.each(questions, function (i, datum) {
    console.log(datum);
    let col = $("<div class= 'col-md-12'>");
    let internal_row = $("<div class= 'row centered quiz_question_entry'>");
    let question_link = $("<a class='listing'>");
    let question_id = datum["id"];
    if (answered.includes(Number(question_id))) {
      console.log(question_id);
      $(question_link).html("Question " + question_id + " &#10004");
    } else {
      $(question_link).html("Question " + question_id);
    }

    //image implementation for questions
    //let question = question_bank[key];
    //let question_img = $("<img class='ycsmallpic' src='"+question["img"]+"' alt='flower1'></img>");
    //$("#quiz_img").append(question_img);


    $(question_link).attr("href", "/quiz/" + question_id);
    $(internal_row).append(question_link);

    $(col).append(internal_row);
    $(row).append(col);
  });

  $("#quiz_questions_listing").append(row);
}

function newQuestions() {
  $.ajax({
    type: "POST",
    url: "/quiz/new",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify({
    }),
    success: function () {
      window.location.href = "/quiz/new";
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
}



$(document).ready(function () {
  loadQuestions(questions);

  $("#new_quiz_button").click(function (event) {
    window.location.href = "/quiz/new";
    event.preventDefault();

  });
});
