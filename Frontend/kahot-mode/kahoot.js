// url = "http://county-contracts.gl.at.ply.gg:7614";
url = "";

correct = -1;
correct_name = "";

async function generateQuestion() {
    res = fetch(url + "/random?size=4");
    d = await res;
    data = await d.json();

    random_rock = Math.floor(Math.random() * Object.keys(data).length);
    correct = random_rock;
    correct_name = data[String(random_rock)]["name"];
    img = url + "/image?filename=" + data[String(random_rock)]["paths"][0];

    console.log(random_rock);

    document.getElementById("question").src = img;
    document.getElementById("1").innerHTML = data["0"]["name"];
    document.getElementById("2").innerHTML = data["1"]["name"];
    document.getElementById("3").innerHTML = data["2"]["name"];
    document.getElementById("4").innerHTML = data["3"]["name"];
    // document.getElementById("result").innerHTML = "";
}

function submit(i) {
    if (i == correct) {
        document.getElementById("result").innerHTML = "correct";
    }
    else {
        document.getElementById("result").innerHTML = "incorrect, correct answer: " + correct_name;
    }
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

generateQuestion();