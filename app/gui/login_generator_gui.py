import dearpygui.dearpygui as dpg
from ..utils.theme_util import *
from ..functions.login_generator_functions import *

def login_render_gui():
    dpg.add_text("------------------------ Gerador de logins --------------------------")
    dpg.add_spacer(height=10)
    
    dpg.add_text("Usuário das contas:")
    dpg.add_input_text(default_value="cordeiro", tag="input_user_login")
    dpg.add_spacer(height=7)

    dpg.add_text("Senha das contas:")
    dpg.add_input_text(default_value="joao1234", tag="input_pass_login")
    dpg.add_spacer(height=7)

    dpg.add_text("Quantidade de contas:")
    dpg.add_drag_int(default_value=1, max_value=999, min_value=1, tag="input_amount_login")
    dpg.add_spacer(height=7)

    with dpg.group(horizontal=True):
        dpg.add_text("Status:")
        dpg.add_input_text(width=201, default_value="Não iniciado", tag="status_login_id")

    with dpg.group(horizontal=True):
        generate_btn = dpg.add_button(label="Criar", width=70, callback=generate_logins)
        show_acc = dpg.add_button(label="Ver logins criados", width=180, callback=show_created_logins)

    dpg.bind_item_theme(generate_btn, btn_green)
    dpg.bind_item_theme(show_acc, btn_yellow)
