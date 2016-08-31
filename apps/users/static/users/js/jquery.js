$(document).ready(function() {
    $('#create_form').submit(function(event) {
        event.preventDefault();
        $.ajax({
            url: "{% url 'index' %}",
            method: "post",
            data: $(this).serialize(),
            success: function(serverResponse) {
                $('#user_table').html(serverResponse);
            }
        });
    });
});
