$(document).ready(function(){
    //search bar //
    $(".active").click(function(){
        $(".search-box").toggle('medium');
    });
    // arrow functionality in products to go back to the top//
    $("#top-arrow").click(function(){
        window.scrollTo(0,0)
    })
});