import { board } from "./board_action.js";

const finishedLoseGame = document.querySelector("#finished-lose-game");
const continueLoseBtns = document.querySelectorAll(".continue-lose-btn")

window.onload = function() {
    finishedLoseGame.style.display = "block";
    board.style.display = "none";
};

let switchToBoard = () => {
    finishedLoseGame.style.display = "none";
    board.style.display = "block";
}

continueLoseBtns.forEach(continueLoseBtn => {
    continueLoseBtn.addEventListener("click", switchToBoard)
});
