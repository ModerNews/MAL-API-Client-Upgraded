// JavaScript Document

$(document).ready(function(){   
	if ($.cookie('accepted_cookies') == 1 ) { 
		$('.cookie').removeClass('cookie').addClass('d-none');
    }
});

document.getElementById("accept-cookies").onclick = function () {
    $.cookie("accepted_cookies", 1);
    $('.cookie').removeClass('cookie').addClass('d-none');
	return false;
};

document.getElementById("close-cookies").onclick = function () {
    $.removeCookie("accepted_cookies");
    $('.cookie').removeClass('cookie').addClass('d-none');
    return false;
};
