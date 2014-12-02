/* Functions to allow CSRF Token to be approved through database updates with AJAX */

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
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

function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/* Bootstrap functions */

$(function () {
  $('[data-toggle="tooltip"]').tooltip()
});

/* X-Editable functions */

$.fn.editable.defaults.mode = 'inline';

/* Custom functions */

function togglefav() {
    $bid = $(this).attr('bid');
    $.ajax({
        url: '/blist/' + $bid + '/mod_fav_bl/',
        method: 'POST',
        success: function() {
            if ($("a[bid=" + $bid + "]").attr('fav') == '0') {
                $("a[bid=" + $bid + "]").attr('fav','1');
                $("a[bid=" + $bid + "]").empty();
                $("a[bid=" + $bid + "]").append('<span bid="' + $bid + '" class="glyphicon glyphicon-star togfav" aria-hidden="true"></span>');
            } else {
                $("a[bid=" + $bid + "]").attr('fav','0');
                $("a[bid=" + $bid + "]").empty();
                $("a[bid=" + $bid + "]").append('<span bid="' + $bid + '" class="glyphicon glyphicon-star-empty togfav" aria-hidden="true"></span>');
            };
        },
    });
};

function toggledone() {
    $oid = $(this).attr('oid');
    $bid = $(this).attr('bid');
    $now = moment().format('MMM. D, YYYY');
    $.ajax({
        url: '/blist/' + $bid + '/' + $oid + '/finish/',
        method: 'POST',
        success: function() {
            if ($("a[oid=" + $oid + "]").attr('fin') == '0') {
                $('a[oid=' + $oid + ']').attr('fin','1');
                $('a[oid=' + $oid + ']').empty();
                $('a[oid=' + $oid + ']').append('<span class="glyphicon glyphicon-check finish" aria-hidden="true" oid="' + $oid + '" bid="' + $bid + '" data-placement="left" data-toggle="tooltip" title="Completed: ' + $now + '"></span> ');
                $('[data-toggle="tooltip"]').tooltip();
            } else {
                $('a[oid=' + $oid + ']').attr('fin','0');
                $('a[oid=' + $oid + ']').empty();
                $('a[oid=' + $oid + ']').append('<span class="glyphicon glyphicon-unchecked finish" aria-hidden="true" oid="' + $oid + '" bid="' + $bid + '"></span> ');
            };
        },
    });
};
