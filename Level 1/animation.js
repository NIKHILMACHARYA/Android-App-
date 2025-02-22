// Initialize toast when the page loads
let toastInstance;
document.addEventListener('DOMContentLoaded', () => {
    animateText();
    // Initialize the toast
    const toastEl = document.getElementById('messageToast');
    toastInstance = new bootstrap.Toast(toastEl, {
        animation: true,
        autohide: true,
        delay: 3000
    });
});

function animateText() {
    const welcomeText = document.querySelector('.welcome-text');
    welcomeText.style.animation = 'none';
    welcomeText.offsetHeight; // Trigger reflow
    welcomeText.style.animation = 'fadeInUp 1s ease-out forwards';
}

function showMessage() {
    // Show the toast message
    toastInstance.show();
    // Also animate the welcome text
    animateText();
}