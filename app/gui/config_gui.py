import dearpygui.dearpygui as dpg
from ..utils.theme_util import *
from ..functions.config_functions import *

def config_render_gui():
    dpg.add_text("-------------------------- Configurações ----------------------------")
    dpg.add_spacer(height=10)

    dpg.add_text("Clique no botão para carregar e visualizar o modelo de contas atual:")
    btn_model_1 = dpg.add_button(label="Verificar modelo", width=190, callback=lambda: show_model("acc", "0%"))
    dpg.add_spacer(height=10)

    dpg.add_text("Clique no botão para carregar e visualizar o modelo de login atual:")
    btn_model_2 = dpg.add_button(label="Verificar modelo", width=190, callback=lambda: show_model("login", "56%"))
    dpg.add_spacer(height=10)

    dpg.bind_item_theme(btn_model_1, btn_blue)
    dpg.bind_item_theme(btn_model_2, btn_blue)