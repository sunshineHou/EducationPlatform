function get_interview_questions(str) {

    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();

    }
    else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    var c = document.getElementById('questions_module');
    while (c.hasChildNodes()) //当div下还存在子节点时 循环继续
    {
        c.removeChild(c.firstChild);
    }

    xmlhttp.onreadystatechange = function () {
        'use strict';
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            var questions_list = JSON.parse(xmlhttp.responseText);
            console.log(questions_list);
            var items = Object.keys(questions_list);
            var n_node = document.getElementById("questions_module");
            var ul = document.createElement('ul');
            ul.className = 'ul_cs';
            n_node.appendChild(ul);

            for (var i = 0; i < items.length; i++) {
                var li = document.createElement('li');
                var a = document.createElement('a');
                var input = document.createElement('input');

                li.className = 'item';

                a.value = items[i];
                a.name = 'question_title';
                a.innerHTML = items[i];

                input.type = 'checkbox';
                input.name = 'is_release';
                input.checked = 'checked';
                input.value = items[i];
                console.log(items[i], '&');

                ul.appendChild(li);
                li.appendChild(a);
                li.appendChild(input);
            }

        }
    };
    xmlhttp.open("GET", "/get_all_questions?q=" + str, true);
    xmlhttp.send();
}
