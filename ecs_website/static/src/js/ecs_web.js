$(document).ready(function(){
    $("#oneday").click(function(){
        $("#main_training").hide();
        $("#oneday_training").show();
        $("#twoday_training").hide();
        $("#threeday_training").hide();
        $("html, body").animate({scrollTop: 0}, 100);
    });
    $("#twoday").click(function(){
        $("#main_training").hide();
        $("#oneday_training").hide();
        $("#twoday_training").show();
        $("#threeday_training").hide();
        $("html, body").animate({scrollTop: 0}, 100);
    });
    $("#threeday").click(function(){
        $("#main_training").hide();
        $("#oneday_training").hide();
        $("#twoday_training").hide();
        $("#threeday_training").show();
        $("html, body").animate({scrollTop: 0}, 100);
    });
    $('#contact_email').keyup(function() {
       if($(this).val() != '') {
          $('#subscribe').prop('disabled', false);
       }
       else {
          $('#subscribe').prop('disabled', true);
       }
    });
    // $("#search_input").keyup(function(e){
    //     var code = e.which; // recommended to use e.which, it's normalized across browsers
    //     if(code==13)e.preventDefault();
    //     if(code==13 && $("#search_input").val()){
    //         alert($("#main_column").val());
    //         // clear value in search view.
    //         $("#search_input").val('');
    //     }
    // });
});
