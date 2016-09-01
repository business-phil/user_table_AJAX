// Refresh User Table based on filter conditions
$(document).on('submit', '#filter_form', function(event) {
    event.preventDefault();
    var name = $('#name').val();
    var date_from = $('#date_from').val();
    var date_to = $('#date_to').val();
    $.ajax({
        url: "/",
        method: "post",
        data: $(this).serialize(),
        success: function(response) {
            $('#user_table').html(response);
            // Repopulate inputs
            $('#name').val(name);
            $('#date_from').val(date_from);
            $('#date_to').val(date_to);
        }
    });
});

// Update table to reflect page number
$(document).on('click', 'a', function(event) {
    event.preventDefault();
    var pagenum = $(this).text();
    $('#page').val(pagenum);
    $('#filter_form').submit();
});

// Create new user; refresh user table
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
