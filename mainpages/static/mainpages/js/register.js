/**
 * Created by jwn on 21/03/2017.
 */
'use strict';
function register() {
    $('#onlineRegister').click(function () {
        $('#registerOptions').css("display","none");
        $('#userInfo').css("display","block");
    });
    $('#submit-btn').click(function () {
        var validation = true;
        if($('#password').val()!==$('#passwordConfirmation').val()){
            validation = false;
        }
        if($('#userName')===null){
            validation = false;
            
        }
        if(validation){
            $('#registerForm').submit();
        }
    });
}


$(function(){
    register();
});