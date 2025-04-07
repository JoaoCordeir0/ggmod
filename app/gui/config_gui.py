import dearpygui.dearpygui as dpg
from ..utils.theme_util import *
from ..functions.config_functions import *

def config_render_gui():
    dpg.add_text("-------------------------- Configurações ----------------------------")
    dpg.add_spacer(height=10)

    dpg.add_text("Clique no botão para carregar e visualizar o modelo de contas atual:")
    btn_model = dpg.add_button(label="Verificar modelo", width=190, callback=show_model_accounts)
    dpg.add_spacer(height=10)

    dpg.bind_item_theme(btn_model, btn_blue)