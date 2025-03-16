let subMenu = document.getElementById("subMenu")

function toggleMenu() {
    subMenu.classList.toggle("hidden")
}

document.addEventListener("click", function (event) {
    let profilePic = document.querySelector("img[onclick='toggleMenu()']");

    if (!subMenu.contains(event.target) && !profilePic.contains(event.target)) {
        subMenu.classList.add("hidden");
    }

});