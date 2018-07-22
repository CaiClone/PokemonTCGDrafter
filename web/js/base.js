
function setOptions(cards){
    $(".option > img").each(function() {
        let newImage = cards[parseInt($(this).parent().attr('option'))];
        $(this).attr('src',newImage);
     });
}
function fillSets(sets){
    const sg = $("#SetGrid");
    sg.append(
            `<div class="card" value="FB">
                <img class="card-img-top setimg" src="https://images.pokemontcg.io/sm6/logo.png">
            </div>`
        );
}
$(document).ready(function(){
    fillSets();
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
$(".setimg").click(function(){
   $(this).toggleClass("bg-primary"); 
});
$("#btnGoDraft").click(function(){
    let sets = $(".bg-primary").parent().map(function() {return $(this).attr('value');});
    eel.getOptions()(function(){
        setOptions();
        $("#SetSelector").hide();
        $("#CardSelector").show();
    });
    
})