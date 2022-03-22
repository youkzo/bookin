// 모달팝업창
$(function(){
    $("#store_register_btn").click(function(){
        $(".modal").show();
        console.log('hello');
    })
})
$(function(){

        // .modal안에 button을 클릭하면 .modal닫기
        $(".modal button").click(function(){
            $("#store_register").hide();
            location.reload();
            console.log('reloaded')
        });
    });


// 도서등록 모달팝업창
$(function(){
    $("#book_upload_btn").click(function(){
        $("._modal").show();
        console.log('hello');
    })
})
$(function(){

        // .modal안에 button을 클릭하면 .modal닫기
        $("._modal button").click(function(){
            $("#upload_books").hide();
            location.reload();
            console.log('reloaded')
        });
    });



