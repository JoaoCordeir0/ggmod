import platform

def get_width_and_height():
    if platform.system() == "Linux":
        return 500, 370
    return 520, 420