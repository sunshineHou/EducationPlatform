jQuery.Huifold = function(obj,obj_c,speed,obj_type,Event){
    if (obj_type == 2) {
        $(obj+":first").find("b").html("-");
        $(obj_c+":first").show()
    }
    $(obj).bind(Event,function () {
        if($(this).next().is(":visible")){
            if(obj_type == 2) {
                return false
            }
            else {
                $(this).next().slideUp(speed).end().removeClass("selected");
                $(this).find("b").html("+")
            }
        }
        else {
            if (obj_type == 3) {
                $(this).next().slideDown(speed).end().addClass("selected");
                $(this).find("b").html("-")
            }
            else {
                $(obj_c).slideUp(speed);
                $(obj).removeClass("selected");
                $(obj).find("b").html("+");
                $(this).next().slideDown(speed).end().addClass("selected");
                $(this).find("b").html("-")
            }
        }
    })
};
$(function(){
	$.Huifold("#Huifold1 .item h4","#Huifold1 .item .info","fast",1,"click"); /*5个参数顺序不可打乱，分别是：相应区,隐藏显示的内容,速度,类型,事件*/
});