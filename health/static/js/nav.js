const prof = document.querySelector(".profile-menu__burger");
const dropdown = document.querySelector(".profile-dropdown");

prof.addEventListener("click", function () {
  if (dropdown.style.display !== "none") {
    dropdown.style.right = "-999px";
    dropdown.style.display = "none";
    prof.classList.remove("profile-menu__burger--open");
  } else {
    dropdown.style.right = "0px";
    dropdown.style.display = "flex";
    prof.classList.add("profile-menu__burger--open");
  }
});
