import dearpygui.dearpygui as dpg
from ..utils.theme_util import *
from ..functions.acc_generator_functions import *

def acc_render_gui():
    dpg.add_text("---------------------- Gerador de contas fake -----------------------")
    dpg.add_spacer(height=10)
    
    dpg.add_text("Usuário e e-mail das contas:")
    dpg.add_input_text(default_value="joaovc1", tag="input_user_acc")
    dpg.add_spacer(height=7)

    dpg.add_text("Senha das contas:")
    dpg.add_input_text(default_value="cordeiro3210", tag="input_pass_acc")
    dpg.add_spacer(height=7)

    dpg.add_text("Gerar automático:")
    dpg.add_checkbox(tag="input_check_acc", callback=disable_or_enable_inputs)
    dpg.add_spacer(height=7)

    dpg.add_text("Quantidade de contas:")
    dpg.add_drag_int(default_value=1, max_value=1000, min_value=1, tag="input_amount_acc")
    dpg.add_spacer(height=7)

    with dpg.group(horizontal=True):
        dpg.add_text("Status:")
        dpg.add_input_text(width=201, default_value="Não iniciado", tag="status_acc_id")

    with dpg.group(horizontal=True):
        generate_btn = dpg.add_button(label="Criar", width=70, callback=generate_accounts)
        show_acc = dpg.add_button(label="Ver contas criadas", width=180, callback=show_created_accounts)

    dpg.bind_item_theme(generate_btn, btn_green)
    dpg.bind_item_theme(show_acc, btn_yellow)

def disable_or_enable_inputs():
    if dpg.is_item_enabled("input_user_acc"):
        dpg.disable_item("input_user_acc")
        dpg.disable_item("input_pass_acc")
        dpg.set_value("input_user_acc", "")
        dpg.set_value("input_pass_acc", "")
    else:
        dpg.enable_item("input_user_acc")
        dpg.enable_item("input_pass_acc")
