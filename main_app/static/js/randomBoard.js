document.addEventListener("DOMContentLoaded", function () {
  const board = document.getElementById("isometric");
  const tiles = Array.from(board.getElementsByClassName("tile"));

  // Shuffle tile order
  for (let i = tiles.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [tiles[i], tiles[j]] = [tiles[j], tiles[i]];
  }

  // Re-add newly shuffled tiles back to the board
  tiles.forEach((tile) => {
    board.appendChild(tile);
  });
});
