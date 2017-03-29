/**
 * Created by jwn on 21/03/2017.
 */
'use strict';
function validateForm() {
        console.log("validate form in");
        var validation = true;
        if($('#userName').val()=== ""){
            validation = false;
            $('#userName').next().css('visibility','visible');
            $('#userName').parent().addClass('has-danger');
        }

        if($('#password').val()!==$('#passwordConfirmation').val()){
            validation = false;
        }
        console.log("userName value"+$('#userName').val());
        if($('#userName').val()=== ""){

            validation = false;
        }
        if(validation){
            console.log("validation");
            //$('#registerForm').submit();
        }
}


$(function(){
    $('#onlineRegister').click(function () {
        $('#registerOptions').css("display","none");
        $('#userInfo').css("display","block");
    });
    $('input[type=text]','$password').each(function(){
        $(this).focus(function () {
            $(this).next().css('visibility','hidden');
            $(this).parent().removeClass('has-danger');
        });
    });
    $('#submit-btn').click(validateForm);
});