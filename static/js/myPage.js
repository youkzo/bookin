$(document).on("input", "input:file", function () {
  readURL(this);
});

function readURL(input) {
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      $("#user-img").attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
    openModal();
  }
}

function openModal() {
  const modal = document.getElementById("modal");
  modal.classList.replace("hidden", "block");
}

function closeModal() {
  const modal = document.getElementById("modal");
  modal.classList.replace("block", "hidden");
  window.location.reload();
}

function passwordCanChangeBtn(e) {
  let password = document.getElementById("password");
  let password2 = document.getElementById("password2");
  let profileBtn = document.getElementById("profileBtn");

  password.removeAttribute("disabled");
  password2.removeAttribute("disabled");
  profileBtn.removeAttribute("disabled");

  Eggy({
    title: "비밀번호를 변경하면 로그아웃됩니다",
    message: "비밀번호를 꼭! 기억해주세요",
    type: "warning",
    position: "bottom-right",
  });

  e.classList += " hidden";
}
