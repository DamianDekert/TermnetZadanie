import { board } from "./board_action.js";

const continuteBtn = document.querySelector(".continue-btn");
const finishedWinGame = document.querySelector("#finished-win-game");

window.onload = function() {
    finishedWinGame.style.display = "block";
    board.style.display = "none";
};

let switchToBoard = () => {
    finishedWinGame.style.display = "none";
    board.style.display = "block";
}

continuteBtn.addEventListener("click", switchToBoard)