from PIL import Image
import numpy as np

def load_image():
    image = Image.open("./app/assets/logo.jpg").convert("RGBA")
    image_data = np.asarray(image, dtype=np.float32) / 255.0

    width, height = image.size

    return image_data, width, height