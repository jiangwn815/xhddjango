'use strict';

$(function(){


    console.log("function in");
    $('#actionBtn').click(function(){
        console.log("click in 15");
        var getdata={};
        getdata["picnumber"]=$('#picNumber').val();
        $.getJSON('crawlerpic',getdata, function(re){
            $.each(re,function(key,value){

                console.log(key+":"+value);
            });
        });



    })
     $('#zipBtn').click(function(){
        console.log("click in 25");
        var getdata={};
        getdata["picnumber"]=$('#picNumber').val();
        $.getJSON('bjdata',getdata, function(re){
            $.each(re,function(key,value){

                console.log(key+":"+value);
            });
        });



    })
});