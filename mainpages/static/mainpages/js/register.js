/**
 * Created by jwn on 21/03/2017.
 */
'use strict';
function register() {

    $('#submit-btn').click(function () {
        var validation = true;
        if($('#userName').val()=== ""){
            validation = false;
            $('#userName').next().css('visibility','visible');
            $('#userName').parent().addClass('has-danger');
        }

        if($('#password').val()!==$('#passwordConfirmation').val()){
            console.log("#password value"+$('#password').val());
            validation = false;
        }
        console.log("userName value"+$('#userName').val());
        if($('#userName').val()=== ""){
            console.log("validation userName value"+$('#userName').val());
            validation = false;
            
        }

        if(validation){
            console.log("validation");
            //$('#registerForm').submit();
        }
    });
}


$(function(){
    $('#onlineRegister').click(function () {
        $('#registerOptions').css("display","none");
        $('#userInfo').css("display","block");
    });
    register();
});