const interactEl = document.getElementById("interact");
const optionEl = document.getElementById("interact-option");
const colourEl = document.getElementById("dino-colour");
const imgEl = document.getElementById("dino-img");

const ANIMATIONS = [
    ['Move', 'Blue', 'https://i.imgur.com/r30yWyT.gif'],
    ['Move', 'Pink', 'https://i.imgur.com/ofQisQu.gif'],
    ['Move', 'Grey', 'https://i.imgur.com/ofduhDZ.gif'],
    ['Move', 'Dark Blue', 'https://i.imgur.com/KnivQk6.gif'],
    ['Move', 'Light Grey', 'https://i.imgur.com/mB5Cael.gif'],
    ['Move', 'Red', 'https://i.imgur.com/ubtx9e3.gif'],
    ['Move', 'Orange', 'https://i.imgur.com/hi7IdJQ.gif'],
    ['Move', 'Green', 'https://i.imgur.com/4d59WM3.gif'],
    ['Move', 'Yellow', 'https://i.imgur.com/UmR3tGG.gif'],
    ['Move', 'Dark Green', 'https://i.imgur.com/pOkYBSS.gif'],
    ['Kick', 'Blue', 'https://i.imgur.com/oYEA7h8.gif'],
    ['Kick', 'Pink', 'https://i.imgur.com/EGVamSg.gif'],
    ['Kick', 'Grey', 'https://i.imgur.com/QOSobnm.gif'],
    ['Kick', 'Dark Blue', 'https://i.imgur.com/baXDBQ5.gif'],
    ['Kick', 'Light Grey', 'https://i.imgur.com/rBrGL79.gif'],
    ['Kick', 'Red', 'https://i.imgur.com/tC4RLJk.gif'],
    ['Kick', 'Orange', 'https://i.imgur.com/y9zQ7n6.gif'],
    ['Kick', 'Green', 'https://i.imgur.com/LMKG381.gif'],
    ['Kick', 'Yellow', 'https://i.imgur.com/KggI93y.gif'],
    ['Kick', 'Dark Green', 'https://i.imgur.com/wlSdiLn.gif'],
    ['Dance', 'Blue', 'https://i.imgur.com/LbUYgPQ.gif'],
    ['Dance', 'Pink', 'https://i.imgur.com/wodg8Zd.gif'],
    ['Dance', 'Grey', 'https://i.imgur.com/CdrhCnh.gif'],
    ['Dance', 'Dark Blue', 'https://i.imgur.com/osMCEaz.gif'],
    ['Dance', 'Light Grey', 'https://i.imgur.com/fNkhf6X.gif'],
    ['Dance', 'Red', 'https://i.imgur.com/zHzHJsx.gif'],
    ['Dance', 'Orange', 'https://i.imgur.com/U5rMMbc.gif'],
    ['Dance', 'Green', 'https://i.imgur.com/EgVQG1b.gif'],
    ['Dance', 'Yellow', 'https://i.imgur.com/my6aLEI.gif'],
    ['Dance', 'Dark Green', 'https://i.imgur.com/BytGefT.gif'],
    ['Jump', 'Blue', 'https://i.imgur.com/yf5fJ5B.gif'],
    ['Jump', 'Pink', 'https://i.imgur.com/zb09NvZ.gif'],
    ['Jump', 'Grey', 'https://i.imgur.com/Gz8x7lK.gif'],
    ['Jump', 'Dark Blue', 'https://i.imgur.com/c2ig79X.gif'],
    ['Jump', 'Light Grey', 'https://i.imgur.com/Zke6Aw8.gif'],
    ['Jump', 'Red', 'https://i.imgur.com/WU0Avgw.gif'],
    ['Jump', 'Orange', 'https://i.imgur.com/wf4RYvs.gif'],
    ['Jump', 'Green', 'https://i.imgur.com/r4lyjnb.gif'],
    ['Jump', 'Yellow', 'https://i.imgur.com/QBShht2.gif'],
    ['Jump', 'Dark Green', 'https://i.imgur.com/OTwP04C.gif'],
]


interactEl.addEventListener("click", () => {
  const action = optionEl.value;
  const colour = colourEl.innerText;

  ANIMATIONS.forEach( function(animation) {
    if (animation[0] === action && animation[1] === colour) {
      imgEl.src = animation[2];
    }
  })

});
