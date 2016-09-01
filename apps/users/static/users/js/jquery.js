// Refresh User Table based on filter conditions
$('#form').submit(function(event) {
    event.preventDefault();
    $.ajax({
        url: "/",
        method: "post",
        data: $(this).serialize(),
        success: function(response) {
            $('#user_table').html(response);
        }
    });
});

$('#create_form').submit(function(event) {
    event.preventDefault();
    $.ajax({
        url: "/create",
        method: "post",
        data: $(this).serialize(),
        success: function(response) {
            $('#user_table').html(response);
        }
    });
    // Clear New User form
    $(this).trigger('reset');
});
