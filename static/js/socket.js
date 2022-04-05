const socket = io("https://chat.bookin.link:8000", { secure: true });
const input = document.getElementById("input");
const messageBox = document.getElementById("messageBox");

socket.on("join", (response) => {});
