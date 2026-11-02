(function () {
  var select = document.getElementById("usertype");
  var row = document.getElementById("register-row");
  var link = document.getElementById("register-link");

  function updateRegister() {
    var opt = select.options[select.selectedIndex];
    var url = opt.dataset.register;

    if (!url) {                      // admin: no register option
      row.hidden = true;
      return;
    }
    row.hidden = false;
    link.href = url;
    link.textContent = "Register as " + opt.dataset.label;
  }

  select.addEventListener("change", updateRegister);
  updateRegister();                  // correct state on page load / back button
})();