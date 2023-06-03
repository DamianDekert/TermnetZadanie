export const board = document.querySelector("#board")
const popup = document.querySelector("#popup-welcome-msg")
const starting_btn = document.querySelector(".start-btn")

// Check if the user has visited the page before
if (!localStorage.getItem('visited')) {
    // User is visiting the page for the first time
    // Show the instructions or perform any desired actions
   popup.style.display = "block"
   board.style.display = "none"
  
    // Set the 'visited' flag in localStorage to indicate that the user has visited the page
    localStorage.setItem('visited', 'true');
  }

  let showBoard = () => {
    popup.style.display = "none";
    board.style.display = "block";
  }

  starting_btn.addEventListener("click", showBoard)