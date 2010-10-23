$(document).ready(function() {
    cards = [];
    var nm = new NotificationManager($('body'));
    $('#question').keypress(function(e) {
        if(e.keyCode == '13') {
            $('#answer').focus();
        }
    });
    $('#answer').keypress(function(e) {
        if(e.keyCode == '13') {
            $('#question').focus();
            cards.push([$('#question').val(), $('#answer').val()]);
            nm.show("hello");
            $('#question').add('#answer').text("");
        }
    });
});