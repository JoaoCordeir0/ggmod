import dearpygui.dearpygui as dpg
import textwrap

def about_render_gui():
    dpg.add_text("------------------------------- Sobre -------------------------------")
    dpg.add_spacer(height=10)

    dpg.add_text("GGMod v1.0")
    dpg.add_spacer(height=10)

    text = "GGMod é um mod para o jogo Goodgame Gangster, desenvolvido por João V. Cordeiro. O objetivo do GGMod é fornecer uma interface gráfica para facilitar a criação de contas no jogo. Todos os fins são apenas educacionais e não visam prejudicar o jogo ou seus desenvolvedores. O GGMod é um projeto open-source e está disponível no GitHub. O uso do GGMod é de responsabilidade do usuário e o desenvolvedor não se responsabiliza por qualquer dano causado pelo uso do mod."
    text = textwrap.fill(text, width=70)

    dpg.add_text(text)

    dpg.add_text("Dev by Cordeiro", pos=(190, 300))