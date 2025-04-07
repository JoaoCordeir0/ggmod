import dearpygui.dearpygui as dpg

dpg.create_context()

with dpg.theme() as btn_green:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (0, 127, 110), category=dpg.mvThemeCat_Core)          # Verde base
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (39, 174, 96), category=dpg.mvThemeCat_Core)   # Hover
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (30, 132, 73), category=dpg.mvThemeCat_Core)    # Clicado
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)          # Texto branco

with dpg.theme() as btn_yellow:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (241, 196, 15), category=dpg.mvThemeCat_Core)          # Amarelo base
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (243, 156, 18), category=dpg.mvThemeCat_Core)   # Hover
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (211, 84, 0), category=dpg.mvThemeCat_Core)      # Clique
        dpg.add_theme_color(dpg.mvThemeCol_Text, (33, 33, 33), category=dpg.mvThemeCat_Core)              # Texto preto suave

with dpg.theme() as btn_blue:
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button, (1, 80, 165), category=dpg.mvThemeCat_Core)           # Azul base
        dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, (41, 128, 185), category=dpg.mvThemeCat_Core)  # Hover
        dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, (31, 97, 141), category=dpg.mvThemeCat_Core)    # Clique
        dpg.add_theme_color(dpg.mvThemeCol_Text, (255, 255, 255), category=dpg.mvThemeCat_Core)          # Texto branco
