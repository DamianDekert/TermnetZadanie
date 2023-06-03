const start_session_btn = document.querySelector("#start-btn");
const text_input = document.querySelector("#username");
const menu = document.querySelector("#menu")
const starting_box = document.querySelector("#username_section")


const socket = io({
    autoConnect : false
});

let startSession = () => {
    let username = text_input.value;

    socket.connect();

    socket.on("connect", function() {
        socket.emit("user_join", username);
    })
    
    menu.style.display = "block";
    starting_box.style.display = "none";

}

window.onload = function() {
    // Check if the user is on the "/" page
    if (window.location.pathname === "/") {
      // Remove the 'visited' flag from localStorage
      localStorage.removeItem('visited');
    }
  };

start_session_btn.addEventListener("click", startSession)

