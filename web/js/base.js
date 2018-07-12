$(document).ready(()=>{
    let cnt=0;
    $(".option").each(function() {
       $(this).attr('option',cnt);
        cnt++;
    });
    $(".option").click(function(){
        console.log($(this).attr('option'));
    });
});