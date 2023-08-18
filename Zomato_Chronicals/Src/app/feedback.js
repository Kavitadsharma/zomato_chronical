
// src/app/feedback.js
function submitFeedback() {
    var rating = document.querySelector('input[name="rating"]:checked').value;
    var review = document.getElementById('review').value;

    // Send feedback data to the server (you would implement this part)
    console.log('Submitted Rating:', rating);
    console.log('Submitted Review:', review);
}
