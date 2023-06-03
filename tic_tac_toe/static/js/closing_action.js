window.addEventListener("unload", function() {
    socket.emit("user_exit");
});
