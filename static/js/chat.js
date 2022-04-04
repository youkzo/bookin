function scrollDown() {
  $("#messageBox").scrollTop($("#messageBox")[0].scrollHeight);
}

function toRecentMessage() {
  document.getElementById("messageBox").scroll({
    top: document.getElementById("messageBox").scrollHeight,
    left: 0,
    behavior: "smooth",
  });
}

function messageInputChange(e) {
  let sendBtn = document.getElementById("sendBtn");
  if (e.value != "") {
    sendBtn.removeAttribute("disabled");
  } else {
    sendBtn.setAttribute("disabled", "disabled");
  }
}

function sendPress(e) {
  if (e.keyCode == 13 && !e.shiftKey) {
    document.getElementById("sendBtn").click();
  }
}
