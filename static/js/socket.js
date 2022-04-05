const socket = io("http://chat.bookin.link:8000");
const input = document.getElementById("input");
const messageBox = document.getElementById("messageBox");

socket.on("join", (response) => {});
