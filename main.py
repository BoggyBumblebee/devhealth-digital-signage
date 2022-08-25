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
from protomatter_dither import process, REDUCE, PASSTHROUGH
import urllib.request
import urllib.error

app = FastAPI()

@app.get(
    "/badges/sonarqube",
    responses = {
        200: {
            "content": {"image/bmp": {}}
        }
    },
    response_class=Response,
)
def read_badges_sonarqube(project: str, metric: str, dither: bool = True):
    url = "https://sonarcloud.io/api/project_badges/measure?project={0}&metric={1}".format(project, metric)
    return read_badges(url, dither)

@app.get(
    "/badges/github",
    responses = {
        200: {
            "content": {"image/bmp": {}}
        }
    },
    response_class=Response,
)
def read_badges_github(account: str, repository: str, dither: bool = True):
    url = "https://github.com/{0}/{1}/actions/workflows/build.yml/badge.svg".format(account, repository)
    return read_badges(url, dither)

def read_badges(url: str, dither: bool):
    try:
        # Import SVG in as a PNG (Stream)
        png = cairosvg.svg2png(url=url)
        img = png # Image.open(BytesIO(png))

        if dither:
            # Perform the gamma correction and error-diffusion dithering on the image, so it looks nice on an 
            # Adafruit Matrix Portal
            bmp = process(img, REDUCE, PASSTHROUGH)
        else:
            # If, no dithering, remove the Alpha from the PNG, as Bitmaps do not have/understand them
            r, g, b, _ = img.split()
            bmp = Image.merge("RGB", (r, g, b))

        # Return the BMP
        return Response(content=image_to_byte_array(bmp), media_type="image/bmp")

    except urllib.error.HTTPError as err:
        raise HTTPException(status_code=404, detail="Badge not found")

def image_to_byte_array(image: Image) -> bytes:
    imgByteArr = BytesIO()
    image.save(imgByteArr, format="bmp")
    imgByteArr = imgByteArr.getvalue()
    return imgByteArr