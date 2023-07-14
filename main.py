import tkinter as tk
import subprocess


def single_player():
    print("Single Player selecionado")

def multiplayer():
    print("Multiplayer selecionado")

def open_single_player_window():
    janela.destroy()
    single_player()

def open_single_player_window():
    janela.destroy()
    subprocess.call(["python3", "Jogo.py"])
    
janela = tk.Tk()
janela.title("Exemplo de Janela")
janela.geometry("600x600")

nome = tk.Label(janela, text="Pedra, Papel e Tesoura", font=("Arial", 20))
nome.pack(pady=10)

btn_single = tk.Button(janela, text="Single Player", command=open_single_player_window, width=20, height=2)
btn_single.pack(pady=10)

btn_multi = tk.Button(janela, text="Multiplayer", command=multiplayer, width=20, height=2)
btn_multi.pack(pady=10)

janela.mainloop()