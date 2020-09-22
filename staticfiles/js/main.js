// CSRF and AJAX configuration
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


// var and func declarations
function scrollfix() {
    $('#output').scrollTop($('#output')[0].scrollHeight);
	$("#input-text").focus();
}

var playerState = {"new_game": true};


// On page load, make a GET request to the server
$( window ).on( "load", function() {
	$.ajax({
		url : "/game/",
		type : "GET",
		success : function(json) {
			$("#output").append(json.outputText);
			playerState = json.playerState;
			scrollfix();
		}
	});
});


// When input is submitted, make a POST request to the server
$('#input').submit(function(event) {
    event.preventDefault();
    $("#output").append("<br>> " + $("#input-text").val() + "<br>");
    $.ajax({
        url : "/game/",
        type : "POST",
		contentType: "application/json; charset=utf-8",
		dataType: "json",
        data : JSON.stringify({"playerState": playerState, "playerCommand": $("#input-text").val()}),
        success : function(json) {
			$("#input-text").val("");
			$("#output").append(json.outputText);
			playerState = json.playerState;
			scrollfix();
        },
        error : function(xhr, errmsg, err) {
            console.log(xhr, errmsg, err);
			$("#input-text").val("");
			$("#output").append("<br>Woops. That wasn't anticipated. Uh... Ignore that, and try again.<br><br>Command?");
			scrollfix();
        }
    });
});

