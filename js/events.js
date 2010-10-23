$(document).ready(function() {
    var nm = new NotificationManager($('body'));
    $('#question').keypress(function(e) {
        if(e.keyCode == '13') {
            $('#answer').focus();
        }
    });
    $('#answer').keypress(function(e) {
        if(e.keyCode == '13') {
            $('#question').focus();
            nm.show("hello");
        }
    });

});