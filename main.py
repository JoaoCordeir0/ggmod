import dearpygui.dearpygui as dpg
from app.gui.acc_generator_gui import acc_render_gui
from app.gui.home_gui import home_render_gui
from app.gui.config_gui import config_render_gui
from app.gui.about_gui import about_render_gui
from app.gui.login_generator_gui import login_render_gui
from app.utils.modal_util import *
from app.utils.screen_util import get_width_and_height

width, height = get_width_and_height()

dpg.create_context()
dpg.create_viewport(title='Goodgame Gangster Mod', width=width, height=height)

def show_window(tag):
    for w in ["home_window", "acc_generator_window", "config_window", "about_window"]:
        dpg.hide_item(w)
    dpg.show_item(tag)

with dpg.window(label="Main", width=width, height=height, pos=(0, 0), no_title_bar=True, no_resize=True, no_move=True, no_collapse=True):
    with dpg.menu_bar():
        with dpg.menu(label="Navegar"):
            dpg.add_menu_item(label="Home", callback=lambda: show_window("home_window"))
            dpg.add_menu_item(label="Gerador de contas", callback=lambda: show_window("acc_generator_window"))
            dpg.add_menu_item(label="Gerador de logins", callback=lambda: show_window("login_generator_window"))
            dpg.add_menu_item(label="Configurações", callback=lambda: show_window("config_window"))

        with dpg.menu(label="Ajuda"):
            dpg.add_menu_item(label="Sobre", callback=lambda: show_window("about_window"))

with dpg.window(tag="home_window", width=width, height=height, pos=(0, 20), no_title_bar=True, no_resize=True, no_move=True, no_collapse=True):
    home_render_gui()

with dpg.window(tag="acc_generator_window", width=width, height=height, pos=(0, 20), no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, show=False):
    acc_render_gui()

with dpg.window(tag="login_generator_window", width=width, height=height, pos=(0, 20), no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, show=False):
    login_render_gui()

with dpg.window(tag="config_window", width=width, height=height, pos=(0, 20), no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, show=False):
    config_render_gui()

with dpg.window(tag="about_window", width=width, height=height, pos=(0, 20), no_title_bar=True, no_resize=True, no_move=True, no_collapse=True, show=False):
    about_render_gui()

show_window("home_window")

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
