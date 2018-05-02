function beforeSubmit(form) {
    if (form.real_name.value == "") {
        alert('用户名不能为空！');
        form.real_name.focus();
        return false;
    }
    if (form.real_name.value.length >= 5) {
        alert('请输入真实名字！');
        form.real_name.focus();
        return false;
    }
    if (form.mobile.value == "") {
        alert('电话号码不能为空！');
        form.mobile.focus();
        return false;
    }
    if (form.mobile.value.length > 11) {
        alert('电话号码不对吧');
        form.mobile.focus();
        return false;
    }
    if (form.mobile.value.length < 11) {
        alert('电话号码不对吧');
        form.mobile.focus();
        return false;
    }
    if (form.height.value == "") {
        alert('身高呢？！');
        form.height.focus();
        return false;
    }
    if (form.height.value > 250) {
        alert('请输入正常的身高!');
        form.height.focus();
        return false;
    }
    if (form.height.value < 50) {
        alert('请输入正常的身高!');
        form.height.focus();
        return false;
    }
    if (form.weight.value == "") {
        alert('体重, 体重~');
        form.weight.focus();
        return false;
    }
    if (form.weight.value.length > 3) {
        alert('请输入正常体重！');
        form.weight.focus();
        return false;
    }
    if (form.weight.value.length < 2) {
        alert('请输入正常体重！');
        form.weight.focus();
        return false;
    }
    if (form.learning.value == "") {
        alert('emmmm, 学习经历~ 多少填点~');
        form.learning.focus();
        return false;
    }
    if (form.allergies.value == "") {
        alert('没有过敏的东西??? 你觉得不填点东西能过得去吗?');
        form.allergies.focus();
        return false;
    }
}