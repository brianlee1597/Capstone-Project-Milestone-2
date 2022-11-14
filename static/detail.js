function empty_all(){
    $("#ycimgdetail").empty();
    $("#ycdetailtitle").empty();
    $("#ycmocotent").empty();
    $("#yccolorcontent").empty();
    //$("#ycback").empty();   
}

function display_details(detail_bank,key){
    //empty old data
    empty_all()
    //insert all new data
    let detail = detail_bank[key];

    //update pic
    let detailimg = $("<img class='ycsmallpic' src='"+detail["img"]+"' alt='"+detail["flowername"]+"'></img>");
    $("#ycimgdetail").append(detailimg);

    //update title
    let detailtitle = $("<span>"+detail["flowername"]+"</span>");
    $("#ycdetailtitle").append(detailtitle);

    //update meanings and origins content
    let flowermo = $("<span>"+detail["meanorigin"]+"</span>");
    $("#ycmocotent").append(flowermo);

    //update colors
    let flowercolor = $("<span>"+detail["colors"]+"</span>");
    $("#yccolorcontent").append(flowercolor);

    //update back button
    //let flowerbutton1= $("<form action='/culture/"+culture["culture_id"]+"<input class='ycbutton' type='submit' value='Back' /></form>");
    //let flowerbutton = $("<button>Back</button>")
    //let flowerbutton2 = $("<input class='ycbutton' type='submit' value='Back' />")
    //let flowerbutton3= $("</form>")

    //$("#ycback").append(flowerbutton1);
    //$("#ycback").append(flowerbutton2);
    //$("#ycback").append(flowerbutton3);
}


$(document).ready(function(){
    display_details(detail_bank,key);

    let detail = detail_bank[key];
    
    $("#backtoculture").click(function() {   
        window.location.href= "/culture/"+ detail["culture_id"] 
    });
    
})