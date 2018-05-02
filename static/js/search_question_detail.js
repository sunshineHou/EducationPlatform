/**
 * 分页函数
 * pno--页数
 * psize--每页显示记录数
 * 分页部分是从真实数据行开始，因而存在加减某个常数，以确定真正的记录数
 * 纯js分页实质是数据行全部加载，通过是否显示属性完成分页功能
 **/

// var title_arr = new Array();
// var answer_arr = new Array();

function goPage(pno, psize) {
    // var title = document.getElementById('title');
    // var answer = document.getElementById('answer');
    // var result_title = title.value();
    // var result_answer = answer.value();
    // title_arr.push(result_title);
    // answer_arr.push(result_answer);

    var itable = document.getElementById("idData");
    var num = itable.rows.length;//表格所有行数(所有记录数)
    console.log(num);
    var totalPage = 0;//总页数
    var pageSize = psize;//每页显示行数
    //总共分几页 
    if (num / pageSize > parseInt(num / pageSize)) {
        totalPage = parseInt(num / pageSize) + 1;
    } else {
        totalPage = parseInt(num / pageSize);
    }
    var currentPage = pno;//当前页数
    var startRow = (currentPage - 1) * pageSize + 1;//开始显示的行  31
    var endRow = currentPage * pageSize;//结束显示的行   40
    endRow = (endRow > num) ? num : endRow;
    40
    console.log(endRow);
    //遍历显示数据实现分页程？'] ['adsdaddasadssadsadjkadjk
    for (var i = 1; i < (num + 1); i++) {
        var irow = itable.rows[i - 1];
        if (i >= startRow && i <= endRow) {
            irow.style.display = "block";
        } else {
            irow.style.display = "none";
        }
    }
    var pageEnd = document.getElementById("pageEnd");
    var tempStr = "共" + num + "题 分" + totalPage + "页 当前第" + currentPage + "题";
    if (currentPage > 1) {
        // tempStr += "<a href=\"#\" onClick=\"goPage("+(1)+","+psize+")\">第一道题</a>";
        // tempStr += "<a href=\"#\" onClick=\"goPage("+(currentPage-1)+","+psize+")\">上一题&nbsp</a>"
    }
    else {
        // tempStr += " 第一道题";
        // tempStr += " <上一题";
    }

    if (currentPage < totalPage) {
        tempStr += "<a href=\"#\" onClick=\"goPage(" + (currentPage + 1) + "," + psize + ")\">下一题></a>";
        // tempStr += "<a href=\"#\" onClick=\"goPage("+(totalPage)+","+psize+")\">最后一题</a>";
    }
    else {
        tempStr += "下一题>";
        tempStr += "<input type='submit' value='提交'>";
    }

    document.getElementById("barcon").innerHTML = tempStr;

}


function submit_answers(title_arr, answer_arr) {

    var xmlhttp;
    if (window.XMLHttpRequest) {
        // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
        xmlhttp = new XMLHttpRequest();

    }
    else {
        // IE6, IE5 浏览器执行代码
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange = function () {
        'use strict';
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {

            xmlhttp.onreadystatechange = state_Change;

        }
    };
    xmlhttp.open("GET", "/submit_interviewquestions_answer?q=" + title_arr + answer_arr, false);
    xmlhttp.send();
}