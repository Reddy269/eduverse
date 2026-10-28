
  var form = document.getElementById("register-form");
  var message = document.getElementById("register-message");
  var password = document.getElementById("password");
  var confirmPassword = document.getElementById("confirm_password");

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

    const csrfToken = form.querySelector("[name=csrfmiddlewaretoken]").value;

    try {
      // Same URL path as the page, so the role comes from the URL on the server.
      const res = await fetch(window.location.pathname, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify(payload),
      });
      const data = await res.json();

      if (res.ok) {
        window.location.href = "/login/";
      } else {
        message.textContent = data.error || "Could not create your account.";
        message.hidden = false;
      }
    } catch (err) {
      message.textContent = "Something went wrong. Please try again.";
      message.hidden = false;
    }
  });
