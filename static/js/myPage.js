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

function changeView(e) {
  if (e.id == "to_edit") {
    document.getElementById("to_edit").classList.add("border-blue-900");
    document.getElementById("to_rented").classList.remove("border-blue-900");
    document.getElementById("edit_profile").classList.remove("hidden");
    document.getElementById("rented_list").classList.add("hidden");
  } else if (e.id == "to_rented") {
    document.getElementById("to_edit").classList.remove("border-blue-900");
    document.getElementById("to_rented").classList.add("border-blue-900");
    document.getElementById("edit_profile").classList.add("hidden");
    document.getElementById("rented_list").classList.remove("hidden");
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
  let passwordBtn = document.getElementById("passwordBtn");

  password.removeAttribute("disabled");
  password2.removeAttribute("disabled");
  profileBtn.removeAttribute("disabled");
  passwordBtn.setAttribute("disabled", "disabled");

  Eggy({
    title: "비밀번호를 변경하면 로그아웃됩니다",
    message: "비밀번호를 꼭! 기억해주세요",
    type: "warning",
    position: "bottom-right",
  });
}

function checkInvalidPassword() {
  Eggy({
    title: "비밀번호 형식을 맞춰주세요.",
    message:
      "비밀번호는 대﹒소문자 포함, 특수문자 포함, 숫자포함 8자이상 입니다.",
    type: "warning",
    position: "bottom-right",
  });
}
