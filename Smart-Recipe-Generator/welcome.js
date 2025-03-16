document.addEventListener("DOMContentLoaded", function () {
    // Select all navbar links
    const navLinks = document.querySelectorAll(".menu li a, .dropdown-content li a");
    
    navLinks.forEach(link => {
        link.addEventListener("click", function (event) {
            event.preventDefault(); // Prevent default behavior
            window.location.href = "login(C231457).html"; // Redirect to login page
        });
    });
});