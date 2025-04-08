import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title="Alerta", width=400, height=200)

with dpg.window(label="Alerta", pos=(95, 80), modal=True, show=False, tag="alert_modal-model-not-found", no_title_bar=False, no_move=True):
    dpg.add_text("Modelo de contas não encontrado!")
    dpg.add_spacer(height=12)
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=225)
        dpg.add_button(label="Fechar", callback=lambda: dpg.configure_item("alert_modal-model-not-found", show=False))

with dpg.window(label="Alerta", pos=(95, 80), modal=True, show=False, tag="alert_modal-generated-accounts-not-found", no_title_bar=False, no_move=True):
    dpg.add_text("Contas inexistentes, clique em criar!")
    dpg.add_spacer(height=12)
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=225)
        dpg.add_button(label="Fechar", callback=lambda: dpg.configure_item("alert_modal-generated-accounts-not-found", show=False))

with dpg.window(label="Alerta", pos=(95, 80), modal=True, show=False, tag="alert_modal-username-not-found", no_title_bar=False, no_move=True):
    dpg.add_text("Informe o usuário para as contas!")
    dpg.add_spacer(height=12)
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=225)
        dpg.add_button(label="Fechar", callback=lambda: dpg.configure_item("alert_modal-username-not-found", show=False))

with dpg.window(label="Alerta", pos=(90, 80), modal=True, show=False, tag="alert_modal-len-username-not-found", no_title_bar=False, no_move=True):
    dpg.add_text("Usuário e senha deve ter entre 4 e 10 letras!")
    dpg.add_spacer(height=12)
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=255)
        dpg.add_button(label="Fechar", callback=lambda: dpg.configure_item("alert_modal-len-username-not-found", show=False))

with dpg.window(label="Alerta", pos=(95, 80), modal=True, show=False, tag="alert_modal-password-not-found", no_title_bar=False, no_move=True):
    dpg.add_text("Informe a senha para as contas!")
    dpg.add_spacer(height=12)
    with dpg.group(horizontal=True):
        dpg.add_spacer(width=225)
        dpg.add_button(label="Fechar", callback=lambda: dpg.configure_item("alert_modal-password-not-found", show=False))