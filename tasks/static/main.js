jQuery(function($) {

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

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var add_to_list = function(card) {
        console.log(card.status + card.title + ": " + card.description)
        var $li = $('<li>');
        $li.text(card.title + ": " + card.description);
        if (card.status == 'Urgent') {
            $li.appendTo($('#urgent'))
        } else if (card.status == 'Complete') {
            $li.appendTo($('#complete'))
        } else {
            $li.appendTo($('#inProgress'))
        }
    }

    $.get('http://localhost:8000/api/tasks/', function(cards) {
        cards.results.forEach(add_to_list)
        });

    var $card = $('#card');
    var $title = $('input[name="title"]');
    var $description = $('textarea[name="description"]');
    var $status = $('select[name="status"]');


    $card.submit(function() {
        console.log('you submitted the form');
        data = {'title': $title.val(), 'description': $description.val(), 'status': $status.val()};

        $.post('http://localhost:8000/api/tasks/', data, add_to_list)

        // $.ajax({
        //     method: 'post',
        //     url: 'http://localhost:8000/api/tasks/',
        //     data: data,
        //     success: add_to_list
        // });
        return false;
    });
})
