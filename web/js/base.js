
function setOptions(cards){
    $(".option > img").each(function() {
        let newImage = cards[parseInt($(this).parent().attr('option'))];
        $(this).attr('src',newImage);
     });
}
function fillSets(sets){
    const sg = $("#SetGrid");
    for (let s of sets){
        sg.append(
                `<div class="card p-2 setCard" value="${s[0]}">
                    <div class="row">
                        <div class="col-auto">
                            <img class="img-fluid setimg" src="${s[2]}">
                        </div>
                        <div class="col-auto">
                            <h5>${s[1]}</h5>
                        </div>
                    </div>
                </div>`
            );
    }
    $(".setCard").click(function(){
        $(this).toggleClass("bg-primary"); 
     });
}
$(document).ready(function(){
    eel.getSets()(fillSets);
    let cnt=0;
    $(".option").each(function() {
       $(this).attr('option',cnt);
        cnt++;
    });
    $(".option").click(function(){
        eel.selectOption($(this).attr('option'))(setOptions);
    });
    
    eel.expose(updateTeam);
    function updateTeam(team){
        $("#deck").val(team.join("\n"));     
    }
});
$("#btnGoDraft").click(function(){
    let sets = $(".bg-primary").map(function() {return $(this).attr('value');});
    eel.setSets()(function(options){
        setOptions(options);
        $("#SetSelector").hide();
        $("#CardSelector").show();
    });
    
})