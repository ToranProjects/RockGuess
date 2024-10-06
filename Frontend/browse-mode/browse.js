data = {}

// url = "http://county-contracts.gl.at.ply.gg:7614"
url = "";

async function getData() {
    res = fetch(url + "/whole");
    js = await res;
    data = await js.json();
    console.log(data);
    // Function to render the rock list
    const rockList = document.getElementById('rock-list');

    // Loop through the data data
    for (const key in data) {
        const rock = data[key];
        console.log(rock);
        const rockItem = document.createElement('div');
        rockItem.classList.add('rock-item');

        const img = document.createElement('img');
        img.src = url + "/image?filename=" + rock.paths[0]; // assuming each rock has at least one image

        const name = document.createElement('h3');
        name.textContent = rock.name;

        // Append image and name to rock item div
        rockItem.appendChild(img);
        rockItem.appendChild(name);

        // Append rock item to the container
        rockList.appendChild(rockItem);
    }
}

getData()