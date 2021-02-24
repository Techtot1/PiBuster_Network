document.getElementById("Thingy").addEventListener("click", () => { eel.get_date() }, false);


eel.expose(prompt_alerts);

function prompt_alerts(description) {
    alert(description);
}