/****************************** [index] ******************************/
// 시작하기 버튼 클릭하면 다음 화면으로 이동
var start_button = document.getElementById('start_button');
        
// 시작하기 버튼 누르면 화면 이동
function start(){
    window.location.href = '/first_choice';
}

// 처음으로 이동
function back(){
    window.location.href = '/index';
}

// 선택지 클릭시 대기화면으로 이동
function loading(value){
    window.location.href = '/loading/' + value;
}

// 마지막 결과화면으로 이동
function result(value){
    window.location.href = '/result/' + value;
}