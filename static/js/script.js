$(document).ready(function(){
    //search bar //
    $(".active").click(function(){
        $(".search-box").toggle('medium');
    });
    // arrow functionality in products to go back to the top//
    $("#top-arrow").click(function(){
        window.scrollTo(0,0)
    })


     // Disable +/- buttons outside 1-99 range
    function enableDisableButton(itemId) {
        var presentValue = parseInt($(`#id_qty_${itemId}`).val());
        var minusDisabled = presentValue < 2;
        var plusDisabled = presentValue > 98;
        $(`#decrement-qty_${itemId}`).prop('disabled', minusDisabled);
        $(`#increment-qty_${itemId}`).prop('disabled', plusDisabled);
    }

    // Ensure proper enabling/disabling of all inputs on page load
    var allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        var itemId = $(allQtyInputs[i]).data('item_id');
        enableDisableButton(itemId);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        var itemId = $(this).data('item_id');
        enableDisableButton(itemId);
    });

    // Increment quantity
    $('.increment-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var presentValue = parseInt($(closestInput).val());
       $(closestInput).val(presentValue + 1);
       var itemId = $(this).data('item_id');
       enableDisableButton(itemId);
    });

    // Decrement quantity
    $('.decrement-qty').click(function(e) {
       e.preventDefault();
       var closestInput = $(this).closest('.input-group').find('.qty_input')[0];
       var presentValue = parseInt($(closestInput).val());
       $(closestInput).val(presentValue - 1);
       var itemId = $(this).data('item_id');
       enableDisableButton(itemId);
    });
});