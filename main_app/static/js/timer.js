const countdownEl = document.getElementById("countdown");
const durationEl = document.getElementById("timer-length");
const startEl = document.getElementById("start-timer");
const pauseEl = document.getElementById("pause-timer");
const cancelEl = document.getElementById("cancel-timer");
const hatchEl = document.getElementById("result");
const formDurationEl = document.getElementById("id_duration");
const eggEl = document.getElementById("egg-move");

let countdownInterval;
let isPaused = false;

// Timer function
function startCountdown(duration) {

  // Removes the 1 second delay when starting timer
  const mins = Math.floor(duration / 60);
  const secs = duration % 60;
  countdownEl.textContent = `${mins < 10 ? "0" : ""}${mins}:${secs < 10 ? "0" : ""}${secs}`;
  formDurationEl.value = `${mins < 10 ? "0" : ""}${mins}:${secs < 10 ? "0" : ""}${secs}`;
  duration--;
  document.title = `${mins < 10 ? "0" : ""}${mins}:${secs < 10 ? "0" : ""}${secs} - Dino Park`;

  // Countdown timer with 1 second intervals
  countdownInterval = setInterval(() => {
    if (!isPaused) {
      const mins = Math.floor(duration / 60);
      const secs = duration % 60;
      countdownEl.textContent = `${mins < 10 ? "0" : ""}${mins}:${secs < 10 ? "0" : ""}${secs}`;
      document.title = `${mins < 10 ? "0" : ""}${mins}:${secs < 10 ? "0" : ""}${secs} - Dino Park`;
      duration--;

      //  Timer is finished
      if (duration < 0) {
        clearInterval(countdownInterval);
        countdownEl.classList.add("hidden");
        pauseEl.classList.add("hidden");
        cancelEl.classList.add("hidden");
        hatchEl.classList.remove("hidden");
        document.title = `Dino Park`;
        eggEl.src = "https://i.imgur.com/WmiKqC3.gif";
      }
    }
  }, 1000);
}

// Start timer
startEl.addEventListener("click", () => {
  startEl.classList.add("hidden");
  durationEl.classList.add("hidden");
  pauseEl.classList.remove("hidden");
  cancelEl.classList.remove("hidden");
  startCountdown(durationEl.value);
});

// Pause timer
pauseEl.addEventListener("click", () => {
  if (!isPaused) {
    isPaused = true;
    pauseEl.textContent = "Start";
  } else {
    isPaused = false;
    pauseEl.textContent = "Pause";
  }
});

// Cancel timer
cancelEl.addEventListener("click", () => {
  clearInterval(countdownInterval);
  countdownEl.textContent = "00:00";
  hatchEl.classList.add("hidden");
  pauseEl.classList.add("hidden");
  pauseEl.textContent = "Pause";
  cancelEl.classList.add("hidden");
  startEl.classList.remove("hidden");
  durationEl.classList.remove("hidden");
  document.title = `Dino Park`;
  isPaused = false;
});
