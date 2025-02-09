from typing import Union
import cv2 as cv
import numpy as np
import io
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import StreamingResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("salam")
def salam():
    return "علیک سلام حبیبی"

@app.get("/salam/{fName}")
def salam1(fName):
    return "علیک سلام " + fName + " " + " حبیبی"

@app.get("/salam/{fName}/{lName}")
def salam2(fName, lName):
    return "علیک سلام " + fName + " " + lName + " حبیبی"

@app.get("/tv-channel/{name}")
def test(name: Union[str, int]):
    return {"name": name}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/create-img/{red}/{green}/{blue}")
def create_img(red: int, green: int, blue: int):
    if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
        img = np.zeros((300, 200, 3), dtype=np.uint8)
        img[:, :] = (red, green, blue)
        img = cv.cvtColor(img, cv.COLOR_RGB2BGR)
        #cv.imwrite("test.jpg", img)
        _, encoded_img = cv.imencode(".png", img)
        
        return StreamingResponse(io.BytesIO(encoded_img.tobytes()), media_type="image/png")
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                              detail="numbers must be between 0 and 255")
    


