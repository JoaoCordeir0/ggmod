import dearpygui.dearpygui as dpg
import os
import textwrap

def show_model_accounts():
    model_path = "./models/model_acc.spt"

    if not os.path.exists(model_path):
        dpg.configure_item("alert_modal-model-not-found", show=True)
        return

    with open(model_path, "rb") as f:
        data = f.read()

    text = data.decode("latin1")

    text = repr(text.split("0%")[0] + '0%')
    text = textwrap.fill(text, width=50)

    with dpg.window(label="Modelo de contas"):
        dpg.add_text(text)
