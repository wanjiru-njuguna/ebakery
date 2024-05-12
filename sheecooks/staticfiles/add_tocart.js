// document.addEventListener('DOMContentLoaded', function () {
//     document.getElementById('add_to_cart').addEventListener('submit', function (event) {
//         event.preventDefault(); // Prevent default form submission

//         // Submit form using AJAX
//         fetch('/add_menu_tocart/', {
//             method: 'POST',
//             headers: {
//                 'X-CSRFToken': '{{ csrf_token }}',
//             },
//             body: new FormData(this),
//         })
//         .then(response => response.json())
//         .then(data => {
//             if (data.success) {
//                 alert(data.message); // Display success message
//             } else {
//                 alert('Failed to add item to cart.'); // Display error message
//             }
//         })
//         .catch(error => {
//             console.error('Error:', error);
//             alert('An error occurred. Please try again.'); // Display error message
//         });
//     });
// });
