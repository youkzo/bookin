const socket = io("http://13.125.253.9:8000");
const input = document.getElementById("input");
const messageBox = document.getElementById("messageBox");

socket.on("join", (response) => {});
