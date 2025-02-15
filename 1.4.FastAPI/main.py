from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.responses import RedirectResponse, StreamingResponse
import cv2 as cv
import numpy as np
import io

app = FastAPI()
friends = {}


@app.get("/")
def read_root():
    return "Hi! Welcome to my API."

@app.get("/items")
def read_friends():
    return {"items": friends}

@app.post("/items")
def add_friend(id: str = Form(), name: str = Form(), age: float = Form()):
    friends[id] = {"name": name, "age": age}
    return friends[id]

@app.delete("/items/{id}")
def remove_friend(id: str):
    if id not in friends:
        raise HTTPException(status_code=404, detail="item not found")
    del friends[id]
    return {"message": "Item deleted"}

@app.put("/items/{id}")
def update_friend(id: str, name: str = Form(None), age: float = Form(None)):
    if id not in friends:
        raise HTTPException(status_code=404, detail="item not found")
    if name is not None:
        friends[id]["name"] = name
    if age is not None:
        friends[id]["age"] = age

    return friends[id]

@app.post("/rgb2gray/")
async def rgb2gray(input_file: UploadFile = File(None)):
    if not input_file.content_type.startswith("image/"):
        raise HTTPException(status_code=415, detail="Unsupported media type")
    
    contents = await input_file.file.read()
    np_array = np.frombuffer(contents, dtype=np.uint8)
    img_rgb = cv.imdecode(np_array, cv.IMREAD_UNCHANGED)

    #process image
    image_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)

    _, img_encoded = cv.imencode(".jpg", image_gray)
    image_bytes = img_encoded.tobytes()
    return StreamingResponse(io.BytesIO(image_bytes), media_type="image/jpeg")
