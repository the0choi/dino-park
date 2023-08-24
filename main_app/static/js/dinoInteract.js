const interactEl = document.getElementById("interact");
const optionEl = document.getElementById("interact-option");
const colourEl = document.getElementById("dino-colour");
const imgEl = document.getElementById("dino-img");

const ANIMATIONS = [
    ['Move', 'Blue'],
    ['Move', 'Pink'],
    ['Move', 'Grey'],
    ['Move', 'Dark Blue'],
    ['Move', 'Light Grey'],
    ['Move', 'Red'],
    ['Move', 'Orange'],
    ['Move', 'Green'],
    ['Move', 'Yellow'],
    ['Move', 'Dark Green'],
    ['Kick', 'Blue'],
    ['Kick', 'Pink'],
    ['Kick', 'Grey'],
    ['Kick', 'Dark Blue'],
    ['Kick', 'Light Grey'],
    ['Kick', 'Red'],
    ['Kick', 'Orange'],
    ['Kick', 'Green'],
    ['Kick', 'Yellow'],
    ['Kick', 'Dark Green'],
    ['Dance', 'Blue'],
    ['Dance', 'Pink'],
    ['Dance', 'Grey'],
    ['Dance', 'Dark Blue'],
    ['Dance', 'Light Grey'],
    ['Dance', 'Red'],
    ['Dance', 'Orange'],
    ['Dance', 'Green'],
    ['Dance', 'Yellow'],
    ['Dance', 'Dark Green'],
    ['Jump', 'Blue'],
    ['Jump', 'Pink'],
    ['Jump', 'Grey'],
    ['Jump', 'Dark Blue'],
    ['Jump', 'Light Grey'],
    ['Jump', 'Red'],
    ['Jump', 'Orange'],
    ['Jump', 'Green'],
    ['Jump', 'Yellow'],
    ['Jump', 'Dark Green'],
]


interactEl.addEventListener("click", () => {
  const action = interactEl.value;
  const colour = colourEl.innerText;

  

  imgEl.src = 

});
