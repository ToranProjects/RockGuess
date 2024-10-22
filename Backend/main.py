import os, uvicorn, json, random
from fastapi import FastAPI
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

data = {}

# Allow all CORS requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open(os.path.join(os.getcwd(), "Backend", "data.json"), encoding="UTF-8") as file:
    data = json.loads(file.read())

@app.get("/image")
def f(filename:str):
    path = os.path.join(os.getcwd(), "Backend", "Images", filename)
    return FileResponse(status_code=200, path=path)

@app.get("/random")
def f(size: int | None = None):
    d = data.copy()
#    print("test random funkce", len(d), len(data))
    if size:
        res = {}
        for i in range(0, size):
            image_data, d = get_random_image_data(dat=d)
            res[i] = image_data
        return JSONResponse(res, status_code=200)
    else:
        return JSONResponse(get_random_image_data(dat=d)[0], status_code=200)

@app.get("/")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "index.html"))

@app.get("/style.css")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "style.css"))

@app.get("/browse-mode/index.html")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "browse-mode", "index.html"))

@app.get("/browse-mode/browse.js")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "browse-mode", "browse.js"))

@app.get("/kahot-mode/index.html")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "kahot-mode", "index.html"))

@app.get("/kahot-mode/kahoot.js")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "kahot-mode", "kahoot.js"))

@app.get("/kahot-mode/kahoot-styles.css")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "kahot-mode", "kahoot-styles.css"))

@app.get("/guess-mode/index.html")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "guess-mode", "index.html"))

@app.get("/guess-mode/guess.js")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "guess-mode", "guess.js"))

@app.get("/guess-mode/guess-styles.css")
def f():
    return FileResponse(os.path.join(os.getcwd(), "Frontend", "guess-mode", "guess-styles.css"))

@app.get("/whole")
def f():
    return JSONResponse(data, status_code=200)

def get_random_image_data(dat):
#   print(len(dat), len(data), dat.keys())
    r = random.randint(0, len(dat.keys()) - 1)
    obj = dat.pop(list(dat.keys())[r])
    return obj, dat

if __name__ == "__main__":
    uvicorn.run(app, port=9999)
