// JavaScript Document

var dots = window.setInterval( function() {
    var wait = document.getElementById("dots");
    if ( wait.innerHTML.length > 2 ) 
        wait.innerHTML = ".";
    else 
        wait.innerHTML += ".";
    }, 250);