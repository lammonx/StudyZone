alert("js开始");
console.log("控制台开始");

function set_h1() {
    document.write("<h1>JS设置html标题</h1>");
}

function set_user_list() {
    const url_json = 'http://127.0.0.1:8086/print/print_json';
    fetch(url_json).then(res => res.json().then(res_json => set_json(res_json)));
    // post Json报文
    // fetch("http://127.0.0.1:8086/print/print_name0", {
    //     method: 'POST',
    //     headers: {
    //         "Content-type": "application/json; charset=UTF-8",
    //     },
    //     body: JSON.stringify({
    //         "name": "111",
    //         "value": "222"
    //     }),
    // }).then(res => res.json().then(res_json => console.log(res_json)));
    // post Data报文
    // fetch("http://127.0.0.1:8086/print/print_name0", {
    //     method: 'POST',
    //     headers: {
    //         "Content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    //     },
    //     body: 'foo=bar&lorem=ipsum',
    // }).then(res => res.json().then(res_json => console.log(res_json)));
    const user_list = document.getElementById('user_list')

    function set_json(res_json) {
        for (let dept in res_json) {
            let user_json = res_json[dept]
            user_list.innerHTML += dept
            for (let userid in user_json) {
                const username = user_json[userid];
                // console.log(userid);
                // console.log(username);
                user_list.innerHTML += "<a id='login_url' href='http://127.0.0.1:8086/print/print_name?name=" + userid + "' target='_blank'>" + username + " </a>";
            }
            user_list.innerHTML += "<br>"
        }
    }
}

function set_btn_events() {
    const btn = document.getElementById("set_env");
    btn.onclick = function () {
        alert("被点击了");
        alert(btn.innerText)
        btn.innerText = "xxx"
        alert(btn.innerHTML);
        const as = document.getElementsByTagName("a");
        for (let i = 0; i < as.length; i++) {
            let a = as[i]
            // a.innerHTML = "666"
            a.href += '666'
        }
    };
}

window.onload = function () {
    set_user_list()
    set_btn_events();
}

//
// let a = {
//     "A": "啊啊",
//     "B": "宝宝",
//     "C": "尺寸"
// }
// for (let key in a) {
//     document.writeln("<option value=\"" + key + "\">" + a[key] + "</option>")
// }
// let b = {
//     "xuw": "徐#伟",
//     "liym": "李#萌",
//     "wangxg": "王#纲"
// }
// for (let key in b) {
//     document.writeln("<option value=\"" + key + "\">" + b[key] + "</option>")
// }