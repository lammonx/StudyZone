let now_env = ""

function set_env_list() {
    function handle(res_json) {
        const env_list = document.getElementById('env_list')
        let envs = res_json["envs"]
        this.now_env = envs[0]
        for (let index in envs) {
            env_list.innerHTML += "<option value=\"" + envs[index] + "\">" + envs[index] + "</option>"
        }
    }

    fetch("http://127.0.0.1:8086/login/get_env_list").then(res => res.json().then(res_json => handle(res_json)));
}

function set_env_select_events() {
    const env_select = document.getElementById("env_list");
    env_select.onchange = function () {
        const as = document.getElementsByTagName("a");
        for (let i = 0; i < as.length; i++) {
            let a = as[i]
            a.href = a.href.split("&env=")[0]
            a.href += "&env=" + env_select.value
        }
    }
}

function set_user_list() {

    function handle(res_json) {
        const user_list = document.getElementById('user_list')
        for (let dept in res_json) {
            let user_json = res_json[dept]
            user_list.innerHTML += dept + "："
            for (let userid in user_json) {
                const username = user_json[userid];
                user_list.innerHTML += "<a id='login_url' href='http://127.0.0.1:8086/login/quick_login?user_id=" + userid + "&env=one.rzzl' target='_blank'>" + username + " </a>";
            }
            user_list.innerHTML += "<br>"
        }
    }

    fetch("http://127.0.0.1:8086/login/get_user_id").then(res => res.json().then(res_json => handle(res_json)));
}

function set_btn_events() {

    const quick_login = document.getElementById("quick_login");
    const common_login = document.getElementById("common_login");

    quick_login.onclick = function () {

        const user_name = document.getElementById("user_name").value;
        // 通过接口获取id
        let user_id;

        // .replace("#", "%23")
        fetch("http://127.0.0.1:8086/login/get_user_id?user_name=" + encodeURIComponent(user_name)).then(res => res.json().then(res_json => set_user_id(res_json)));

        function set_user_id(res_json) {
            for (const resJsonKey in res_json) {
                for (const resJsonKeyKey in res_json[resJsonKey]) {
                    user_id = resJsonKeyKey;
                    let url = "http://127.0.0.1:8086/login/quick_login?user_id=" + user_id + "&env=st";
                    window.open(url);
                }
            }
        }
    };
    common_login.onclick = function () {

        const user_name = document.getElementById("user_name").value;
        // 通过接口获取id
        let user_id;

        // .replace("#", "%23")
        fetch("http://127.0.0.1:8086/login/get_user_id?user_name=" + encodeURIComponent(user_name)).then(res => res.json().then(res_json => set_user_id(res_json)));

        function set_user_id(res_json) {
            for (const resJsonKey in res_json) {
                for (const resJsonKeyKey in res_json[resJsonKey]) {
                    user_id = resJsonKeyKey;
                    let url = "http://127.0.0.1:8086/login/common_login?user_id=" + user_id + "&env=st";
                    window.open(url);
                    url = "http://127.0.0.1:8086/login/common_login_with_token"
                    window.open(url);
                }
            }
        }
    };
}

window.onload = function () {
    set_env_list();
    set_env_select_events();
    set_user_list();
    set_btn_events();
}

// post
// Json报文
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