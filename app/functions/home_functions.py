import os
import sys
from PIL import Image
import numpy as np

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def load_image():
    image_path = resource_path("app/assets/logo.jpg")
    image = Image.open(image_path).convert("RGBA")
    image_data = np.asarray(image, dtype=np.float32) / 255.0

    width, height = image.size
    return image_data, width, height