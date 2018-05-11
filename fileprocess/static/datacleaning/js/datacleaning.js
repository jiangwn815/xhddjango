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
    });
    $('#collectxlsBtn').click(function(){
        console.log("click in collectxlsBtn");
        var getdata={};
        getdata["picnumber"]=$('#picNumber').val();
        $.getJSON('collectxls',getdata, function(re){
            $.each(re,function(key,value){

                console.log(key+":"+value);
            });
        });
    });
     $('#zipBtn').click(function(){
        console.log("click in 25");
        var getdata={};
        getdata["picnumber"]=$('#picNumber').val();
        $.getJSON('bjdata',getdata, function(re){
            $.each(re,function(key,value){

                console.log(key+":"+value);
            });
        });
     });

     $('#dealXlsx').click(function(){
        console.log("click in dealxlsx");
        var getdata={};
        getdata["picnumber"]=$('#picNumber').val();
        $.getJSON('dealxlsx',getdata, function(re){
            $.each(re,function(key,value){

                console.log(key+":"+value);
            });
        });
    });
});