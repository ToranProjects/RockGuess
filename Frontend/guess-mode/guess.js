// url = "http://county-contracts.gl.at.ply.gg:7614";
url = "";

data = {}
correct_name = ""

async function generateQuestion() {
    res = fetch(url + "/random");
    d = await res;
    data = await d.json();
    // console.log(data);
    correct_name = data["name"]

    img = url + "/image?filename=" + data["paths"][0];
    document.getElementById("question").src = img;
}

function editString(str) {
    str = str.replace(/\s+/g, '');
    str = str.toLowerCase();
    str = str.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    return str;
}

function submit(i) {
    correct = false;

    t = data["aliases"]
    console.log(i);
    for (j = 0; j < t.length; j++) {
        if (t[j] == editString(i)) {
            correct = true;
        }
    }

    if (correct) {
        document.getElementById("result").innerHTML = "correct";
    }
    else {
        document.getElementById("result").innerHTML = "incorrect, correct answer: " + correct_name;
    }
    document.getElementById("input").value = ""
    clearResult();
    generateQuestion();
}

function clearResult() {
    setTimeout(() => {
        document.getElementById("result").innerHTML = "";
    }, 3000);
}

function returnHome() {
    window.location.assign('/');
}

$(document).ready(function () {

    $('.input').keydown(function (event) {
        // enter has keyCode = 13, change it if you want to use another button
        if (event.keyCode == 13) {
            submit(document.getElementById("input").value);
            return false;
        }
    });

});

generateQuestion();