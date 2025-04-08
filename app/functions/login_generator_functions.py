import dearpygui.dearpygui as dpg
import os
import textwrap
import time
import subprocess
import tempfile
import platform

def generate_logins(status_id):    
    username = str(dpg.get_value("input_user_login"))
    len_usernmae = len(username)
    password = str(dpg.get_value("input_pass_login"))
    len_password = len(password)
    amount = int(dpg.get_value("input_amount_login"))

    if not username:
        dpg.configure_item("alert_modal-username-not-found", show=True)
        return
    
    if len_usernmae < 4 or len_usernmae > 10 or len_usernmae != len_password:
        dpg.configure_item("alert_modal-len-username-not-found", show=True)
        return
    
    if not password:
        dpg.configure_item("alert_modal-password-not-found", show=True)
        return   
    
    model_path = f"./models/model_login_{len_usernmae}.spt"

    if not os.path.exists(model_path):
        dpg.configure_item("alert_modal-model-not-found", show=True)
        return
    
    with tempfile.TemporaryDirectory() as temp_dir:
        dpg.set_value(status_id, "Criando logins...")

        with open(model_path, "rb") as f:
            data = f.read()

        text = data.decode("latin1")

        index = 1
        for item in text.split("5556%"):
            nomenclature = f"{username}{index:03}"
            correct_text = item + "5556%"
            new_text = correct_text.replace((len_usernmae * "X") + "001", nomenclature).replace(len_usernmae * "Z", password)
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

        with open("./generated_logins.spt", "wb") as f:
            f.write(merged_data)

        dpg.set_value(status_id, "Logins criados com sucesso!")

        if platform.system() == "Linux":
            subprocess.run(["xdg-open", os.getcwd()])
        else:
            subprocess.run(["explorer", os.getcwd()])

def show_created_logins():
    generate_logins_path = "./generated_logins.spt"
    
    if not os.path.exists(generate_logins_path):
        dpg.configure_item("alert_modal-generated-accounts-not-found", show=True)
        return

    with open(generate_logins_path, "rb") as f:
        data = f.read()

    text = data.decode("latin1")

    split_text = text.split("5556%")

    text_start = repr(split_text[0] + '5556%')
    text_start = textwrap.fill(text_start, width=50)

    text_end = repr(split_text[len(split_text)-2] + '5556%')
    text_end = textwrap.fill(text_end, width=50)

    with dpg.window(label="Primeira conta criada"):
        dpg.add_text(default_value=text_start)

    with dpg.window(label="Última conta criada", pos=(0, 130)):
        dpg.add_text(default_value=text_end)