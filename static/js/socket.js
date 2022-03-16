const socket = io("http://localhost:8000");

socket.on("join", (response) => {
  console.log(response);
});

socket.on("sendMessage", (msg) => {
  console.log(msg);
});
