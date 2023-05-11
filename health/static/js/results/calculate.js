const result = document.getElementById("result");
if (localStorage.getItem("result")) {
  result.innerHTML = localStorage.getItem("result");
}
const age = document.getElementById("age");
const weight = document.getElementById("weight");
const height = document.querySelector("#height");
const goal = document.querySelector("#goal");
const activity = document.querySelector("#activity");
let gender = NaN;
document.getElementById("sex").addEventListener("change", function (even) {
  var radios = document.getElementsByName("gender");
  for (let i = 0, length = radios.length; i < length; i++) {
    if (radios[i].checked) {
      res = radios[i].value;
      break;
    }
  }
  if (res === "мужчина") {
    gender = 1;
  } else {
    if (res === "женщина") {
      gender = 0.8;
    } else {
      gender = NaN;
    }
  }
  console.log("gender", gender);
  document.getElementById("calculating").click();
});
document
  .getElementById("calculating")
  .addEventListener("click", function (even) {
    if (
      age.value &&
      weight.value &&
      height.value &&
      goal.value &&
      activity.value &&
      gender
    ) {
      let button = document.getElementById("calculateButton");
      button.disabled = false;
    }
  });
// здесь подставляются значения по умолчанию
var currentAge = String(document.getElementById("currentAge").innerHTML);
if (currentAge) {
  age.value = currentAge;
}
var currentWeight = String(document.getElementById("currentWeight").innerHTML);
if (currentWeight) {
  weight.value = currentWeight;
}
var currentHeight = String(document.getElementById("currentHeight").innerHTML);
if (currentHeight) {
  height.value = currentHeight;
}

function calculate(age, weight, height, gender) {
    let callories = NaN
  if (gender == 1) {
    callories = String(
      Math.round(Math.floor((9.99 * weight) + (6.25 * height) - (4.92 * age) + 5.0))
    );
  } else {
    callories = String(
      Math.round(Math.floor((10 * weight) + (6.25 * height) - (4.92 * age) - 161.0))
    );
  }

  result.innerHTML = callories;
  localStorage.setItem("result", callories);
  saveData();
}

document
  .getElementById("calculating")
  .addEventListener("input", function (event) {
    // console.log('age', age.value, 'weight', weight.value, 'height', height.value, 'goal', goal.value, 'activity', activity.value, 'gender',  gender)

    if (
      age.valueAsNumber &&
      weight.valueAsNumber &&
      height.valueAsNumber &&
      parseFloat(goal) &&
      parseFloat(activity) &&
      gender
    ) {
      let button = document.getElementById("calculateButton");
      button.disabled = false;
    }
  });
document
  .getElementById("calculating")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    calculate(
      age.valueAsNumber,
      weight.valueAsNumber,
      height.valueAsNumber,
      parseFloat(goal.value),
      parseFloat(activity.value),
      gender
    );
  });

function saveData() {
  let data = {
    target: parseFloat(goal.value),
    dailyCalories: result.innerHTML,
  };
  if (!currentHeight) {
    data["height"] = height.valueAsNumber;
  }
  if (!currentWeight) {
    data["weight"] = weight.valueAsNumber;
  }
  if (!currentAge) {
    data["age"] = age.valueAsNumber;
  }
  console.log("data", data);
  fetch("/accounts/set_data/", {
    method: "POST",
    body: JSON.stringify(data),
  });
}
