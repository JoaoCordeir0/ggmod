import dearpygui.dearpygui as dpg
import os
import textwrap
import time
import subprocess
import tempfile
import platform

def generate_accounts(status_id):
    model_path = "./models/model_acc.spt"

    if not os.path.exists(model_path):
        dpg.configure_item("alert_modal-model-not-found", show=True)
        return
    
    username = str(dpg.get_value("input_user_acc"))
    password = str(dpg.get_value("input_pass_acc"))
    amount = int(dpg.get_value("input_amount_acc"))

    if not username:
        dpg.configure_item("alert_modal-username-not-found", show=True)
        return
    
    if not password:
        dpg.configure_item("alert_modal-password-not-found", show=True)
        return    
    
    with tempfile.TemporaryDirectory() as temp_dir:
        dpg.set_value(status_id, "Criando contas...")

        with open(model_path, "rb") as f:
            data = f.read()

        text = data.decode("latin1")

        index = 1
        array = text.split("0%")
        array.pop()
        for item in array:
            nomenclature = f"{username}{index:03}"
            correct_text = item + "0%"
            new_text = correct_text.replace("jotinha101", nomenclature).replace("Ronaldinho12", password)
            index += 1

            new_binary = new_text.encode("latin1")
            with open(f"{temp_dir}/a_{nomenclature}.spt", "wb") as f:
                f.write(new_binary)

        time.sleep(0.5)
                
        merged_data = b""

        for i in range(1, amount + 1):
            filename = f"{temp_dir}/a_{username}{i:03}.spt"
            with open(filename, "rb") as f:
                merged_data += f.read()

        with open("./generated_accounts.spt", "wb") as f:
            f.write(merged_data)

        dpg.set_value(status_id, "Contas criadas com sucesso!")

        if platform.system() == "Linux":
            subprocess.run(["xdg-open", os.getcwd()])
        else:
            subprocess.run(["explorer", os.getcwd()])

def show_created_accounts():
    generate_accounts_path = "./generated_accounts.spt"
    
    if not os.path.exists(generate_accounts_path):
        dpg.configure_item("alert_modal-generated-accounts-not-found", show=True)
        return

    with open(generate_accounts_path, "rb") as f:
        data = f.read()

    text = data.decode("latin1")

    split_text = text.split("0%")

    text_start = repr(split_text[0] + '0%')
    text_start = textwrap.fill(text_start, width=50)

    text_end = repr(split_text[len(split_text)-2] + '0%')
    text_end = textwrap.fill(text_end, width=50)

    with dpg.window(label="Primeira conta criada"):
        dpg.add_text(default_value=text_start)

    with dpg.window(label="Última conta criada", pos=(0, 150)):
        dpg.add_text(default_value=text_end)