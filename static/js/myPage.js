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
  }
}

function passwordCanChangeBtn(e) {
  let password = document.getElementById("password");
  let password2 = document.getElementById("password2");

  password.removeAttribute("disabled");
  password2.removeAttribute("disabled");
  Eggy({
    title: "비밀번호를 변경하면 로그아웃됩니다",
    message: "비밀번호를 꼭! 기억해주세요",
    type: "warning",
  });
  e.classList += " hidden";
}
