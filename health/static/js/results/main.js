const btnStart = document.getElementById("beforeChange");
const btnNew = document.getElementById("currentWeightBtn");
const btnIdea = document.getElementById("ideaChange");
const modalNew = document.querySelector(".new");
const modalStart = document.querySelector(".start");
const modalIdea = document.querySelector(".idea");
const modalC1 = document.querySelector(".modal-c-1");
const modalC2 = document.querySelector(".modal-c-2");

const modalC3 = document.querySelector(".modal-c-3");
const modalC4 = document.querySelector(".modal-c-4");

const enterNew = document.querySelector(".new button");
const enterStart = document.querySelector(".start button");
const enterIdea = document.querySelector(".idea button");

btnStart.addEventListener("click", () => {
  modalStart.style.display = "block";
  modalC2.style.display = "block";
});
btnNew.addEventListener("click", () => {
  modalNew.style.display = "block";
  modalC1.style.display = "block";
});
btnIdea.addEventListener("click", () => {
  modalIdea.style.display = "block";
  modalC3.style.display = "block";
});
enterNew.addEventListener("click", (even) => {
  let input = document.querySelector(".new input").valueAsNumber;
  sendWeight("new", input);
  modalNew.style.display = "none";
});

enterStart.addEventListener("click", (even) => {
  let input = document.querySelector(".start input").valueAsNumber;
  sendWeight("start", input);
  modalStart.style.display = "none";
});

enterIdea.addEventListener("click", (even) => {
  let input = document.querySelector(".idea input").valueAsNumber;
  sendWeight("idea", input);
  modalIdea.style.display = "none";
});

function sendWeight(field, value) {
  data = { field: field, value: value };
  fetch("/accounts/set_weight/", {
    method: "POST",
    body: JSON.stringify(data),
  });
}
