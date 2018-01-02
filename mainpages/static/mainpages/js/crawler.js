'use strict';

$(function(){


    console.log("function in");
    $('#actionBtn').click(function(){
        console.log("click in");
        $.getJSON('crawlerpic',function(re){
            $.each(re,function(key,value){

                console.log(key+":"+value);
            });
        });



    })
});