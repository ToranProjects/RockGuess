import os, uvicorn, json, random
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()

data = {}

with open(os.path.join(os.getcwd(), "Backend", "data.json"), encoding="UTF-8") as file:
    data = json.loads(file.read())

@app.get("/image")
def f(filename:str):
    path = os.path.join(os.getcwd(), "Backend", "Images", filename)
    return FileResponse(status_code=200, path=path)

@app.get("/random")
def f(size: int | None = None):
    if size:
        d = data
        res = {}
        for i in range(0, size):
            image_data, d = get_random_image_data(dat=d)
            res[i] = image_data
        return JSONResponse(res, status_code=200)
    else:
        return JSONResponse(get_random_image_data()[0], status_code=200)

@app.get("/")
def f():
    return JSONResponse(data, status_code=200)

@app.get("/whole")
def f():
    return JSONResponse(data, status_code=200)

def get_random_image_data(dat=data):
    r = random.randint(0, len(dat.keys()) - 1)
    obj = dat.pop(list(dat.keys())[r])
    return obj, dat

if __name__ == "__main__":
    uvicorn.run(app, port=8000)