$(document).ready(function() {
    $('#question').keydown(function(e) {
        if(e.keyCode == '13') {
            $('#answer').focus();
        }
    });
    $('#answer').keydown(function(e) {
        if(e.keyCode == '13') {
            $('#question').focus();
        }
    });


});