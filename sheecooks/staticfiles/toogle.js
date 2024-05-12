
function toggleHiddenDiv() {
    var hidden_menu = document.getElementById('hidden_menu');

    // Toggle the visibility of the div
    if (hidden_menu.style.display === 'none') {
        hidden_menu.style.display = 'block';
    } else {
        hidden_menu.style.display = 'none';
    }
}

// Add event listeners to elements
document.getElementById('toggle_bars').addEventListener('click', toggleHiddenDiv);
document.getElementById('cancel_hidden_div').addEventListener('click', toggleHiddenDiv);