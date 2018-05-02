function get_modules(str) {

    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();

    }
    else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    var c = document.getElementById('modules_module');
    while (c.hasChildNodes()) //当div下还存在子节点时 循环继续
    {
        c.removeChild(c.firstChild);
    }

    xmlhttp.onreadystatechange = function () {
        'use strict';
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            var module_list = JSON.parse(xmlhttp.responseText);
            var items = Object.keys(module_list);
            var n_node = document.getElementById("modules_module");
            var b = document.createElement('option');
            b.value = '章节';
            b.innerHTML = '章节';
            n_node.appendChild(b);
            for (var i = 0; i < items.length; i++) {
                console.log(items[i]);
                var a = document.createElement('option');
                a.value = items[i];
                a.innerHTML = items[i];
                a.onclick = get_modules;
                console.log(a, 'hello');
                n_node.appendChild(a)
            }

        }
    };
    xmlhttp.open("GET", "/submit_course_info?q=" + str, true);
    xmlhttp.send();
}


function get_knowledegbases(str) {

    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();

    }
    else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    var c = document.getElementById('knowledgebases_module');
    while (c.hasChildNodes()) //当div下还存在子节点时 循环继续
    {
        c.removeChild(c.firstChild);
    }

    xmlhttp.onreadystatechange = function () {
        'use strict';
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            var knowledge_list = JSON.parse(xmlhttp.responseText);
            var items = Object.keys(knowledge_list);
            var n_node = document.getElementById("knowledgebases_module");
            var b = document.createElement('option');
            b.value = '知识点';
            b.innerHTML = '知识点';
            n_node.appendChild(b);
            for (var i = 0; i < items.length; i++) {
                console.log(items[i]);
                var a = document.createElement('option');
                a.value = items[i];
                a.innerHTML = items[i];
                a.onclick = get_knowledegbases;
                console.log(a, 'hello');
                n_node.appendChild(a)
            }

        }
    };
    xmlhttp.open("GET", "/submit_module_info?q=" + str, true);
    xmlhttp.send();
}

function get_questionbanks(str) {

    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();

    }
    else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    var c = document.getElementById('questionbanks_module');
    while (c.hasChildNodes()) //当div下还存在子节点时 循环继续
    {
        c.removeChild(c.firstChild);
    }

    xmlhttp.onreadystatechange = function () {
        'use strict';
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            var questionbanks_list = JSON.parse(xmlhttp.responseText);
            console.log(questionbanks_list);
            var items = Object.keys(questionbanks_list);
            var n_node = document.getElementById("questionbanks_module");
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
    xmlhttp.open("GET", "/submit_knowledgebase_info?q=" + str, true);
    xmlhttp.send();
}
