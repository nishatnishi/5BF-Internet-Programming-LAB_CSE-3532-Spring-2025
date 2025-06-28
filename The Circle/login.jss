// ✅ AJAX Login with Redirect
const loginForm = document.getElementById("login-form");
loginForm.addEventListener("submit", function (e) {
  e.preventDefault();
  const email = document.getElementById("login-email").value.trim();
  const password = document.getElementById("login-password").value;

  fetch("backend/login.php", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ email, password }),
  })
    .then((res) => res.text())
    .then((data) => {
      if (data.includes("successful")) {
        alert("Login Successful!");
        closeModal();
        // 🔁 Redirect user to dashboard or welcome page
        window.location.href = "dashboard.html";
      } else {
        alert(data);
      }
    });
});
