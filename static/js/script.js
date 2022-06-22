// show login when click on login text and hide register
var button = document.getElementById("loginButton");
button.addEventListener("click", function (e) {
    document.getElementById("login").hidden = false;
    document.getElementById("register").hidden = true;
});

// show register when click on register text and hide login
var button2 = document.getElementById("registerButton");
button2.addEventListener("click", function (e) {
    document.getElementById("login").hidden = true;
    document.getElementById("register").hidden = false;
});