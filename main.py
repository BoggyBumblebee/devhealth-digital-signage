# SPDX-FileCopyrightText: 2022 Christopher Marsh-Bourdon (boggybumblebee)
#
# SPDX-License-Identifier: MIT

"""
DEVELOPMENT HEALTH DIGITAL SIGNAGE for Adafruit Matrix Portal: displays stats about GitHub/SonarQube projects. 
Requires WiFi internet access.

Written by Christopher Marsh-Bourdon (boggybumblebee).
MIT license, all text above must be included in any redistribution.

BDF fonts from the X.Org project.
"""

import cairosvg
from fastapi import FastAPI, HTTPException, Response
from io import BytesIO
from PIL import Image
import urllib.request
import urllib.error

app = FastAPI()

@app.get(
    "/badges",
    responses = {
        200: {
            "content": {"image/bmp": {}}
        }
    },
    response_class=Response,
)
def read_badges(project: str, metric: str):

    # http://127.0.0.1:8000/badges?project=devhealth-digital-signage&metric=alert_status
    # http://127.0.0.1:8000/badges?project=XYZ&metric=XYZ

    url = "https://sonarcloud.io/api/project_badges/measure?project={0}&metric={1}".format(project, metric)

    try:
        # Import SVG in as a PNG (Stream)
        png = cairosvg.svg2png(url=url)
        img = Image.open(BytesIO(png))

        # Remove the Alpha from the PNG, as Bitmaps do not have/understand them
        r, g, b, _ = img.split()
        img = Image.merge("RGB", (r, g, b))

        # Return the BMP
        return Response(content=image_to_byte_array(img), media_type="image/bmp")

    except urllib.error.HTTPError as err:
        raise HTTPException(status_code=404, detail="Badge not found")

def image_to_byte_array(image: Image) -> bytes:
    imgByteArr = BytesIO()
    image.save(imgByteArr, format="bmp")
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr