function checkInvalidPassword() {
  Eggy({
    title: "비밀번호 형식을 맞춰주세요.",
    message:
      "비밀번호는 대﹒소문자 포함, 특수문자 포함, 숫자포함 8자이상 입니다.",
    type: "warning",
    position: "bottom-right",
  });
}
