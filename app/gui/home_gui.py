import dearpygui.dearpygui as dpg
from ..functions.home_functions import load_image

def home_render_gui():
    image_data, width, height = load_image()

    with dpg.texture_registry():
        dpg.add_static_texture(width=width, height=height, default_value=image_data, tag="logo_ggmod")
    
    dpg.add_image("logo_ggmod", pos=(103, 50))
    dpg.add_text("GGMod v1.0", pos=(205, 240))
    dpg.add_text("Dev by Cordeiro", pos=(190, 300))