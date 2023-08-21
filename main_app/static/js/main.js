const countdownEl = document.getElementById('countdown');
const durationEl = document.getElementById('timer-length');
const startEl = document.getElementById('start-timer');
const pauseEl = document.getElementById('pause-timer');
const hatchEl = document.getElementById('result');
const eggEl = document.getElementById('egg')

let countdownInterval;
let isPaused = false;

function startCountdown(duration) {
    
    // Removes the 1 second delay when starting timer
    const mins = Math.floor(duration / 60);
    const secs = duration % 60;
    countdownEl.textContent = `${mins < 10 ? '0' : ''}${mins}:${secs < 10 ? '0' : ''}${secs}`;
    duration--;


    countdownInterval = setInterval(() => {
        if (!isPaused) {
            const mins = Math.floor(duration / 60);
            const secs = duration % 60;
            countdownEl.textContent = `${mins < 10 ? '0' : ''}${mins}:${secs < 10 ? '0' : ''}${secs}`;
            duration--;

            if (duration < 0) {
                clearInterval(countdownInterval);
                countdownEl.textContent = '00:00';
                pauseEl.classList.add('hidden');
                hatchEl.classList.remove('hidden');
            }
        }
        
    }, 1000);
}

startEl.addEventListener('click', () => {
    startEl.classList.add('hidden');
    durationEl.classList.add('hidden');
    eggEl.classList.remove('hidden');
    pauseEl.classList.remove('hidden');
    startCountdown(durationEl.value);
});

pauseEl.addEventListener('click', () => {
    if (!isPaused) {
        isPaused = true;
        pauseEl.textContent = 'Start';

    } else {
        isPaused = false;
        pauseEl.textContent = 'Pause';
    }
});

hatchEl.addEventListener('click', () => {
    const emptyTile = Array.from(tiles).find(tile => !tile.querySelector('a img'));
    if (emptyTile) {
        const dinoImg = document.createElement('img');
        dinoImg.src = 'https://i.imgur.com/OLfpwzO.gif';
        const dinoLink = document.createElement('a');
        dinoLink.href = 'about/';
        dinoLink.appendChild(dinoImg);
        emptyTile.appendChild(dinoLink);
        hatchEl.classList.add('hidden');
    } else {
        console.log('No empty tiles available for hatching.');
    }
});