/**
 * Created by jwn on 21/03/2017.
 */
'use strict';
function validateForm() {
        console.log("validate form in");
        var validation = true;

        $('input[type=text]').each(function () {
            console.log("This value:"+$(this).val());
            if($(this).val()===""){
                validation = false;
                $(this).next().css('visibility','visible');
                $(this).parent().addClass('has-danger');
            }
        });
        if($('#password').val()===""){
            validation = false;
            $('#password').next().css('visibility','visible');
            $('#password').parent().addClass('has-danger');
        }

        if($('#password').val()!==$('#passwordConfirmation').val()){
            validation = false;
            $('#passwordConfirmation').next().css('visibility','visible');
            $('#passwordConfirmation').parent().addClass('has-danger');
        }


        if(validation){
            console.log("validation!!!");
            $('#registerForm').submit();
        }
}


$(function(){
    $('#onlineRegister').click(function () {
        $('#registerOptions').css("display","none");
        $('#userInfo').css("display","block");
    });
    $('input[type=text],#password').each(function(){
        $(this).focus(function () {
            $(this).next().css('visibility','hidden');
            $(this).parent().removeClass('has-danger');
        });
    });

    $('#submit-btn').click(validateForm);
});