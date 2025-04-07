import dearpygui.dearpygui as dpg
import os
import textwrap

def show_model(type, separator):
    model_path = f"./models/model_{type}.spt"

    if not os.path.exists(model_path):
        dpg.configure_item("alert_modal-model-not-found", show=True)
        return

    with open(model_path, "rb") as f:
        data = f.read()

    text = data.decode("latin1")

    text = repr(text.split(separator)[0] + separator)
    text = textwrap.fill(text, width=50)

    with dpg.window(label="Modelo de contas"):
        dpg.add_text(text)