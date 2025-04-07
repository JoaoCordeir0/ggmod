import dearpygui.dearpygui as dpg
from ..utils.theme_util import *
from ..functions.acc_generator_functions import *

def acc_render_gui():
    dpg.add_text("---------------------- Gerador de contas fake -----------------------")
    dpg.add_spacer(height=10)
    
    dpg.add_text("Usuário e e-mail das contas:")
    dpg.add_input_text(default_value="cordeiro", tag="input_user")
    dpg.add_spacer(height=7)

    dpg.add_text("Senha das contas:")
    dpg.add_input_text(default_value="cordeiro321", tag="input_pass")
    dpg.add_spacer(height=7)

    dpg.add_text("Quantidade de contas:")
    dpg.add_slider_int(default_value=1, max_value=1000, min_value=1, tag="input_amount")
    dpg.add_spacer(height=7)

    with dpg.group(horizontal=True):
        dpg.add_text("Status:")
        status_id = dpg.add_input_text(width=201, default_value="Não iniciado")

    with dpg.group(horizontal=True):
        generate_btn = dpg.add_button(label="Criar", width=70, callback=lambda: generate_accounts(status_id))
        show_acc = dpg.add_button(label="Ver contas criadas", width=180, callback=show_created_accounts)

    dpg.bind_item_theme(generate_btn, btn_green)
    dpg.bind_item_theme(show_acc, btn_yellow)
