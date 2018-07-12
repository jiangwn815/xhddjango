'use strict';

$(function(){
    console.log("function in");
    $('#actionBtn').click(function(){
        console.log("click in 15");
        var getdata={};

        $.getJSON('getqrimg',getdata, function(re){
            $.each(re,function(key,value){
                console.log(key+":"+value);
            });
        });
    });

});