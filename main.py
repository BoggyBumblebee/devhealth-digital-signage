import cairosvg
from PIL import Image
from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/badges")
def read_root():

    cairosvg.svg2png(url="https://sonarcloud.io/api/project_badges/measure?project=devhealth-digital-signage&metric=sqale_rating", 
        write_to="images/sqale_rating.png")

    file_in = "images/sqale_rating.png"
    img = Image.open(file_in)

    r, g, b, _ = img.split()
    img = Image.merge("RGB", (r, g, b))
    file_out = "images/sqale_rating.bmp"
    img.save(file_out)
    return {"Saved": "File"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}