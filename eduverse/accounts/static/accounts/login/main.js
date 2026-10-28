// accounts/register/main.js
var form = document.getElementById("register-form");
var message = document.getElementById("register-message");
var password = document.getElementById("password");
var confirmPassword = document.getElementById("confirm_password");

function getCookie(name) {
  var match = document.cookie.match(new RegExp("(^|; )" + name + "=([^;]*)"));
  return match ? decodeURIComponent(match[2]) : null;
}

// Browser-side check only; the server validates again.
function checkMatch() {
  var mismatch = confirmPassword.value && confirmPassword.value !== password.value;
  confirmPassword.setCustomValidity(mismatch ? "Passwords do not match" : "");
}
password.addEventListener("input", checkMatch);
confirmPassword.addEventListener("input", checkMatch);

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  message.hidden = true;

  const payload = {
    name: document.getElementById("name").value.trim(),
    email: document.getElementById("email").value.trim(),
    password: password.value,
    confirm_password: confirmPassword.value,
  };

  try {
    // form.action is the page URL if the form has no action attribute.
    const res = await fetch(form.action, {
      method: "POST",
      credentials: "same-origin",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": getCookie("csrftoken"),
      },
      body: JSON.stringify(payload),
    });

    if (res.ok) {
      window.location.href = "/login/";
      return;
    }

    const data = await res.json().catch(() => ({}));
    message.textContent = data.error || "Could not create your account.";
    message.hidden = false;
  } catch (err) {
    console.error("Register request failed:", err);
    message.textContent = "Something went wrong. Please try again.";
    message.hidden = false;
  }
});