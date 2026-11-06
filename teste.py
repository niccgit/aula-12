import tkinter as tk

janela = tk.Tk()
janela.title("Base fundo branco")
janela.geometry("1920x1080")

janela.configure(bg="white")
rotulo = tk.Label(janela, text="Olá, Tkinter!", bg="white")
rotulo.pack()

janela.mainloop()