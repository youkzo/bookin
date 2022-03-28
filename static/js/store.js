// 스토어등록 & 도서업로드 모달팝업창
$(function(){
    $(".upload").click(function(){
        $("#upload_books").show();
        console.log('hello');
    })
})
$(function(){

        // .modal안에 button을 클릭하면 .modal닫기
        $(".modal button").click(function(){
            $("#upload_books").hide();
            location.reload();
            console.log('refresh')
        });
    });

