let wrapper = document.getElementById("tiles");

let columns = 0;
let rows = 0;
let toggled = false;

const createTile = (index) => {
  const tile = document.createElement("div");
  tile.classList.add("tile");
  tile.style.opacity = toggled ? 0 : 1;
  tile.onclick = () => handleOnClick(index);
  return tile;
};

const createTiles = (quantity) => {
  Array.from(Array(quantity)).map((tile, index) => {
    wrapper.appendChild(createTile(index));
  });
};

const createGrid = () => {
  wrapper.innerHTML = "";
  const size = document.body.clientWidth > 800 ? 100 : 50;
  columns = Math.floor(document.body.clientWidth / size);
  rows = Math.floor(document.body.clientHeight / size);

  wrapper.style.setProperty("--columns", columns);
  wrapper.style.setProperty("--rows", rows);
  createTiles(columns * rows);
};

window.onload = () => createGrid();
window.onresize = () => {
  createGrid();
};

const toggle = () => {
  toggled = !toggled;
  wrapper.classList.toggle("toggled");
};

const handleOnClick = (index) => {
  toggle();

  anime({
    targets: ".tile",
    opacity: toggled ? 0 : 1,
    delay: anime.stagger(50, {
      grid: [columns, rows],
      from: index,
    }),
  });
};
