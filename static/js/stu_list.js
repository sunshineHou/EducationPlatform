function get_stu_list(str) {

    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();

    }
    else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    var c = document.getElementById('student_module');
    while (c.hasChildNodes()) //当div下还存在子节点时 循环继续
    {
        c.removeChild(c.firstChild);
    }

    xmlhttp.onreadystatechange = function () {
        'use strict';
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            var students_list = JSON.parse(xmlhttp.responseText);
            console.log(students_list);
            var items = Object.keys(students_list);
            var n_node = document.getElementById("student_module");
            var ul = document.createElement('ul');
            var form = document.createElement('form');
            form.id = '{{ forloop.counter }}';
            // form.action = '{% url "submit_stu_info" %}';
            // form.method = 'GET';
            ul.className = 'ul_cs';
            n_node.appendChild(ul);


            for (var i = 0; i < items.length; i++) {
                var li = document.createElement('li');
                var a = document.createElement('a');
                var input = document.createElement('input');


                li.className = 'item';

                a.value = items[i];
                a.name = 'student_name';
                a.innerHTML = items[i];
                a.href = "submit_stu_info";

                a.onclick = "document.getElementById('{{ forloop.counter }}').submit()";

                input.name = 'en_name';
                input.value = items[i];
                input.type = 'hidden';

                ul.appendChild(li);
                li.appendChild(a);
                li.appendChild(form);
                li.appendChild(input);
            }

        }
    };
    xmlhttp.open("GET", "/submit_class_info?q=" + str, true);
    xmlhttp.send();
}
