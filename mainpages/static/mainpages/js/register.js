/**
 * Created by jwn on 21/03/2017.
 */
'use strict';
function register() {
    $('#onlineRegister').click(function () {
        $('#registerOptions').css("display","none");
        $('#userInfo').css("display","block");
    });
}


$(function(){
    register();
});