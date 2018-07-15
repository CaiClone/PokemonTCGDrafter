
function setOptions(cards){
    $(".option > img").each(function() {
        let newImage = cards[parseInt($(this).parent().attr('option'))];
        $(this).attr('src',newImage);
     });
}
$(document).ready(function(){
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
    }
    eel.getOptions()(setOptions);
});
$("#deck").val(team.join("\n"));