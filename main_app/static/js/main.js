const timerLengthSelect = document.getElementById('timer-length');
const startTimerButton = document.getElementById('start-timer');
const countdownDisplay = document.getElementById('countdown');
const countdownForm = document.getElementById('countdown-form');
const resultDiv = document.getElementById('result');
const newFormButton = document.getElementById('new-form-button');

let countdownInterval;
let isTimerRunning = false;

function startCountdown(duration) {
    if (isTimerRunning) {
        return;
    }
    
    isTimerRunning = true;
    
    let remainingTime = duration;
    countdownInterval = setInterval(() => {
        const minutes = Math.floor(remainingTime / 60);
        const seconds = remainingTime % 60;
        countdownDisplay.textContent = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
        remainingTime--;

        if (remainingTime < 0) {
            clearInterval(countdownInterval);
            countdownDisplay.textContent = 'Time\'s up!';
            resultDiv.style.display = 'block'; // Show the result div
            isTimerRunning = false;
        }
    }, 1000);
}

startTimerButton.addEventListener('click', () => {
    const selectedDuration = parseInt(timerLengthSelect.value, 10);
    startCountdown(selectedDuration);
});
