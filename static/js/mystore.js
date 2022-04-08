$(document).on("input", "input:file", function () {
  console.log('사진클릭')
  readURL(this);
});

function readURL(input) {
  console.log('redurl함수실행')
  if (input.files && input.files[0]) {
    let reader = new FileReader();
    reader.onload = function (e) {
      $("#currentImage").attr("src", e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
    openModal();
  }
}

// 스토어등록&도서등록 모달팝업창

$(function () {
  $(".modal_popup").click(function () {
    console.log("clicked");
    let pop_val = $(this).attr("value");
    console.log(pop_val);
    $("." + pop_val).show();
  });
  $(".btn").click(function () {
    let close_val = $(this).attr("value");
    console.log(close_val);
    $("." + close_val).hide();
    location.reload();
    console.log("reloaded");
  });
});

// 도서상태수정 팝업창 대여여부 체크박스
$(document).ready(function () {
  console.log("worked");
  // 현재 대여여부 상태를 텍스트로 표기
  if ($("#cb_status").prop("checked")) {
    $("#cb_text").text("대여가능");
  } else {
    $("#cb_text").text("대여중");
  }

  $("#cb_status").click(function () {
    console.log("체크박스클릭");
    // 체크박스 클릭되어있으면 대여가능->대여중으로 변경
    if ($(this).prop("checked")) {
      console.log(document.querySelector("#cb_text").value);
      $("#cb_text").empty();
      $("#cb_text").text("대여가능");
      // $('#cb_status').val('1');
      // $('#cb_status').attr('value','1');
    } else {
      $("#cb_text").empty();
      $("#cb_text").text("대여중");
      // $('#cb_status').val('0');
    }
  });
});
