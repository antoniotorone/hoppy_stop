$(document).ready(function(){
    $(".active").click(function(){
        $(".search-box").toggle('medium');
    });

    $("#top-arrow").click(function(){
        window.scrollTo(0,0)
    })
});