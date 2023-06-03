import { board } from "./board_action.js";

const finishedDrawGame = document.querySelector("#finished-draw-game");
const continueDrawBtn = document.querySelector(".continue-draw-btn")

window.onload = function() {
    finishedDrawGame.style.display = "block";
    board.style.display = "none";
};

let switchToBoard = () => {
    finishedDrawGame.style.display = "none";
    board.style.display = "block";
};

continueDrawBtn.addEventListener("click", switchToBoard)
