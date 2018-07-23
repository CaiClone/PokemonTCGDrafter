
function setOptions(cards){
    $(".option > img").each(function() {
        let newImage = cards[parseInt($(this).parent().attr('option'))];
        $(this).attr('src',newImage);
     });
     $(".option").show();
}
function fillSets(sets){
    const sg = $("#SetGrid");
    for (let s of sets){
        sg.append(
                `<div class="card p-2 setCard" value="${s[0]}">
                    <div class="row">
                        <div class="col-auto">
                            <img class="img-fluid setimg" src="${s[1]}">
                        </div>
                        <div class="col-auto">
                            <h5>${s[0]}</h5>
                        </div>
                    </div>
                </div>`
            );
    }
    $(".setCard").click(function(){
        $(this).toggleClass("bg-primary"); 
     });
}
eel.expose(updateTeam);
function updateTeam(teamstats){
    let team =teamstats[0];
    let teamImages = teamstats[1];
    let count = teamstats[2];
    $("#deck").val(team.join("\n"));
    $("#nCards").text(count);  
}
$(document).ready(function(){
    eel.getSets()(fillSets);
    let cnt=0;
    $(".option").each(function() {
       $(this).attr('option',cnt);
        cnt++;
    });
    $(".option").click(function(){
        $(".option").hide();
        eel.selectOption($(this).attr('option'))(setOptions);
    });
    
    
    $("#btnGoDraft").click(function(){
        let sets = $(".bg-primary").map(function() {return $(this).attr('value');});
        eel.setSets(sets.get())(function(options){
            setOptions(options);
            $("#SetSelector").hide();
            $("#CardSelector").show();
        });
        
    })
});