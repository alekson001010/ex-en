const practice = document.querySelector(".practice");
const meal = document.querySelector(".meal");
const scrab = document.querySelector(".scrab");
const practiceBtn = document.querySelector(".practiceBtn");
const mealBtn = document.querySelector(".mealBtn");
const scrabBtn = document.querySelector(".scrabBtn");

practiceBtn.addEventListener("click", function () {
  if (practice.style.display === "block") {
    practice.style.display = "none";
  } else {
    practice.style.display = "block";
    meal.style.display = "none";
    scrab.style.display = "none";
  }
});

mealBtn.addEventListener("click", function () {
  if (meal.style.display === "block") {
    meal.style.display = "none";
  } else {
    meal.style.display = "block";
    scrab.style.display = "none";
    practice.style.display = "none";
  }
});

scrabBtn.addEventListener("click", function () {
  if (scrab.style.display === "block") {
    scrab.style.display = "none";
  } else {
    scrab.style.display = "block";
    meal.style.display = "none";

    practice.style.display = "none";
  }
});
