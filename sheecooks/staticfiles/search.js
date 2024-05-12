document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('search_form').addEventListener('submit', function(event) {
        event.preventDefault(); 
        var query = document.getElementById('search_bar').value.trim(); // Get the search query
        if (query !== '') {
            window.location.href = '/search/?q=' + encodeURIComponent(query); // Redirect to search URL with query parameter
        }
    });
});
