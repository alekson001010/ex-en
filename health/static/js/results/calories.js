const formCalories = document.getElementById("formCalories");
const btnBreakfast = document.getElementById("breakfast");
const btnLunch = document.getElementById("lunch");
const btnDinnerr = document.getElementById("dinner");
const btnSnack = document.getElementById("snack");
const meal = document.getElementById("meal");
const modalC4 = document.querySelector(".modal-c-4");

btnBreakfast.addEventListener("click", (even) => {
  formCalories.style.display = "block";
  modalC4.style.display = "block";

  meal.value = "breakfast";
});
btnLunch.addEventListener("click", (even) => {
  formCalories.style.display = "block";
  modalC4.style.display = "block";

  meal.value = "lunch";
});

btnDinnerr.addEventListener("click", (even) => {
  formCalories.style.display = "block";
  modalC4.style.display = "block";

  meal.value = "dinner";
});

btnSnack.addEventListener("click", (even) => {
  formCalories.style.display = "block";
  modalC4.style.display = "block";
  meal.value = "snack";
});

// water
const waterDisplay = document.getElementById("waterDisplay");
if (waterDisplay.innerHTML.length === 3) {
  waterDisplay.innerHTML += "0";
}
// const cups = parseFloat(waterDisplay.innerHTML) / 0.25
const cups = document.getElementsByClassName("Cups");
// console.log(cups)
for (let cup of cups) {
  cup.addEventListener("click", (event) => {
    sendWater();
  });
}

function sendWater() {
  fetch("/calculate/set_water/", {
    method: "POST",
  });
  location.reload();
}
