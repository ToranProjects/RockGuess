url = "http://county-contracts.gl.at.ply.gg:7614"

async function generateQuestion(){
    res = fetch(url + "/random?size=4");
    d = await res;
    data = await d.json();

    r = Math.floor(Math.random() * data["0"]["paths"].length);
    img = url + "/image?filename=" + data["0"]["paths"][r];
    
}