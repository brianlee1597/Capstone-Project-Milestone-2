function empty_all(){
    $("#ycculturetitle").empty();
    $("#yccultureintro").empty();
    $("#ycflower1").empty();
    $("#ycflower2").empty();
    $("#ycflower3").empty();
    $("#ycmeaning1").empty();
    $("#ycmeaning2").empty();
    $("#ycmeaning3").empty();
    $("#ycorigins1").empty();
    $("#ycorigins2").empty();
    $("#ycorigins3").empty();
    $("#ycimg1").empty();
    $("#ycimg2").empty();
    $("#ycimg3").empty();
    $("#yclink1").empty();
    $("#yclink2").empty();
    $("#yclink3").empty();
}

function display_details(culture_bank,key){
    //empty old data
   empty_all()
    //insert all new data
    let culture = culture_bank[key];

    //update title
    let culturetitle = $("<span>"+culture["culture"]+"</span>");
    $("#ycculturetitle").append(culturetitle);

    //update intro
    let cultureintro = $("<span>"+culture["intro"]+"</span>");
    $("#yccultureintro").append(cultureintro);
    //update pic
    let cultureimg1 = $("<img class='ycsmallpic' src='"+culture["img1"]+"' alt='flower1'></img>");
    $("#ycimg1").append(cultureimg1);
    let cultureimg2 = $("<img class='ycsmallpic' src='"+culture["img2"]+"' alt='flower2'></img>");
    $("#ycimg2").append(cultureimg2);
    let cultureimg3 = $("<img class='ycsmallpic' src='"+culture["img3"]+"' alt='flower3'></img>");
    $("#ycimg3").append(cultureimg3);

    //update flowername
    let flowername1 = $("<span>"+culture["flower1"]+"</span>");
    $("#ycflower1").append(flowername1);
    let flowername2 = $("<span>"+culture["flower2"]+"</span>");
    $("#ycflower2").append(flowername2);
    let flowername3 = $("<span>"+culture["flower3"]+"</span>");
    $("#ycflower3").append(flowername3);

    //update meanings
    let flowermean1 = $("<span>"+culture["meanings1"]+"</span>");
    $("#ycmeaning1").append(flowermean1);
    let flowermean2 = $("<span>"+culture["meanings2"]+"</span>");
    $("#ycmeaning2").append(flowermean2);
    let flowermean3 = $("<span>"+culture["meanings3"]+"</span>");
    $("#ycmeaning3").append(flowermean3);

    //update origins
    let flowerorigin1 = $("<span>"+culture["origins1"]+"</span>");
    $("#ycorigins1").append(flowerorigin1);
    let flowerorigin2 = $("<span>"+culture["origins2"]+"</span>");
    $("#ycorigins2").append(flowerorigin2);
    let flowerorigin3 = $("<span>"+culture["origins3"]+"</span>");
    $("#ycorigins3").append(flowerorigin3);
  
    //update link
    key1=culture["id"]*3 -2;
    key2=culture["id"]*3 -1;
    key3=culture["id"]*3;
    //console.log(key1);
    //console.log(key2);
    //console.log(key3);
    let link1 = $("<a href='/detail/"+key1+"'>More details</a> ");
    let link2 = $("<a href='/detail/"+key2+"'>More details</a> ");
    let link3 = $("<a href='/detail/"+key3+"'>More details</a> ");
    $("#yclink1").append(link1);
    $("#yclink2").append(link2);
    $("#yclink3").append(link3);
}

$(document).ready(function(){
    display_details(culture_bank,key);

    $("#previous").click(function() {   
        let culture = culture_bank[key];
        if(culture["id"]=="1"){
            window.location.href= "/" 
        }
        else{
            window.location.href= "/culture/"+ String(key-1) 
        }
    });

    $("#next").click(function() {   
        let culture = culture_bank[key];
        if(culture["id"]=="4"){
            window.location.href= "/" 
        }
        else{
            keynext=parseInt(key)+1
            window.location.href= "/culture/"+ String(keynext) 
        }
    });


})