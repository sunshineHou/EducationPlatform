$(document).ready(function(){
// 不用看
    $('.wrapper').slideDown('slow');
    $('#navButton').click(function(){
        $('.menu').slideToggle('slow');
        togglemenu();
    });
// 表单验证
    $("#infobtn").click(
        function () {
            var reg = /^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
            if(reg.test($('#inputemail').val())){

            }else {
                $(".warning").css("display","inline");
                $(".warning").prepend("<p>请输入正确的邮箱!</p>");
            }
        }
    );
});
