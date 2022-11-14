function loadQuestion(){
    $("#question").html("Can you matching flowers with their meanings?")
    $("#flower_name_1").html("lotus")
    $("#flower_name_2").html("lily")
    $("#flower_name_3").html("chrysanthemum")
    $("#flower_name_4").html("orchid")
    $("#meaning_1").html("good fortune and happiness")
    $("#meaning_2").html("symbol of purity")
    $("#meaning_3").html("beauty and elegance")
    $("#meaning_4").html("happiness and vitality")
    $("#flower_picture_1").attr("src", "https://i.ibb.co/8cQ8Ymy/beautiful-lily-varieties-to-grow-4136203-3-ecb49980016c4a498a90d6c379307ddd.jpg")
    $("#flower_picture_2").attr("src", "https://i.ibb.co/8cQ8Ymy/beautiful-lily-varieties-to-grow-4136203-3-ecb49980016c4a498a90d6c379307ddd.jpg")
    $("#flower_picture_3").attr("src", "https://i.ibb.co/8cQ8Ymy/beautiful-lily-varieties-to-grow-4136203-3-ecb49980016c4a498a90d6c379307ddd.jpg")
    $("#flower_picture_4").attr("src", "https://i.ibb.co/8cQ8Ymy/beautiful-lily-varieties-to-grow-4136203-3-ecb49980016c4a498a90d6c379307ddd.jpg")
    $("#hint_1").html("lotus")
    $("#hint_2").html("lily")
    $("#hint_3").html("chrysanthemum")
    $("#hint_4").html("orchid")
}

function checkAnswer(matched){
    console.log(matched)
    let complete = 1
    for (let i = 1; i < 5; i++) {
        if (!matched.includes(i)){
            complete = 0
        }
    }
    if (complete == 0) {
        console.log("Some flower is unmatched with a meaning")
    } else {
        let correct = false
        //TODO check answer
        if (!correct) {
            console.log("show answers")
            $("#matching_hints_container").show("slow")
        }
    }
    
}

function nextQuestion(){
    console.log("next question")  
    next_question_id = parseInt(question["id"])+1
    if (next_question_id <= 5) {
        window.location.href = "/quiz/" + next_question_id
    } else {
        window.location.href = "/score"
    }

}

function selectFlower(prev_flower, matched, colors, curr_flower) {
    if (prev_flower != 0 && matched[prev_flower-1] == 0) {
        $("#selected_flower_"+prev_flower.toString()).css("background-color", "grey")
    }
    $("#selected_flower_"+curr_flower).css("background-color", colors[curr_flower-1])
}

function selectMeaning(flower, matched, colors, selected_meaning) {
    if (flower != 0) {
        if (matched[flower-1] != 0) {
            $("#selected_meaning_"+matched[flower-1].toString()).css("background-color", "grey")
        }
        for (let i = 0; i < 4; i++) {
            if (matched[i] == selected_meaning) {
                $("#selected_flower_"+(i+1).toString()).css("background-color", "grey")
                matched[i] = 0
            }
        }

        $("#selected_meaning_"+selected_meaning.toString()).css("background-color", colors[flower-1])
        matched[flower-1] = selected_meaning
    }
    console.log(matched)

    return matched
}


$(document).ready(function(){
    $("#matching_hints_container").hide()

    let matched = [0, 0, 0, 0]   
    let colors = ["lightgreen", "lightblue", "purple", "cyan"]

    // load question nav link
    for (let i = 1; i < 6; i++) {
        let question_link= $("<a class='listing'>")
        $(question_link).html(i)
        $(question_link).attr("href", "/quiz/" + i)
        if (i==1){
            //$(question_link).css("font-weight", "bold")
            //$(question_link).css("font-size", "25px")
        }
        $("#questions_nav").append(question_link)     
    }                   
    loadQuestion()

    let flower = 0

    $("#selected_flower_1").click(function(){
        selectFlower(flower, matched, colors, 1)
        flower = 1
    })

    $("#selected_flower_2").click(function(){
        selectFlower(flower, matched, colors, 2)
        flower = 2
    })

    $("#selected_flower_3").click(function(){
        selectFlower(flower, matched, colors, 3)
        flower = 3
    })

    $("#selected_flower_4").click(function(){
        selectFlower(flower, matched, colors, 4)
        flower = 4
    })

    $("#selected_meaning_1").click(function(){
        matched = selectMeaning(flower, matched, colors, 1)
        checkAnswer(matched)
    })

    $("#selected_meaning_2").click(function(){
        matched = selectMeaning(flower, matched, colors, 2)
        checkAnswer(matched)
    })

    $("#selected_meaning_3").click(function(){
        matched = selectMeaning(flower, matched, colors, 3)
        checkAnswer(matched)
    })

    $("#selected_meaning_4").click(function(){
        matched = selectMeaning(flower, matched, colors, 4)
        checkAnswer(matched)
    })
    
    
    $("#next_button").click(function(event){      
        nextQuestion()
        event.preventDefault();
    })
    
        

})