function loadScore(current_score) {
  $("#score-report").html(
    `<div class="row"> <h1> &#x1F389; Congratulations! &#x1F389; </h1></div>
    <div class="row" style="margin: auto"> <h5>You got ` +
      current_score +
      " pts!</h5></div>"
  );
  if (top_scores.length > 0) {
    let table = $("<table>");
    table.attr("border", "2px solid #aaa");
    table.attr("width", "100%");
    let i = 1;
    for (const score of top_scores) {
      let row = $("<tr>");
      row.html("<td>" + i + "</td>" + "<td>" + score + "</td>");

      if (score === current_score) {
        row.addClass("highlight-score");
      }
      table.append(row);
      i++;
    }
    $("#topscores").append(table);
  } else {
    $("#topscores").html("No scores at the moment. You can be the first!");
  }
}

$(document).ready(function () {
  loadScore(current_score);
  $("#quiz_button").click(function (event) {
    window.location.href = "/quiz/all";
    event.preventDefault();
  });

  $("#new_quiz_button").click(function (event) {
    window.location.href = "/quiz/new";
    event.preventDefault();
  });

});
