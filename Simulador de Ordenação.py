import tkinter as tk
import random


WIDTH = 800
HEIGHT = 400
NUM_BARRAS = 50
DELAY = 50  

def desenhar_barras(canvas, dados, cores):
    canvas.delete("all")
    largura = WIDTH / len(dados)
    for i, valor in enumerate(dados):
        x0 = i * largura
        y0 = HEIGHT - valor
        x1 = (i + 1) * largura
        y1 = HEIGHT 
        canvas.create_rectangle(x0, y0, x1, y1, fill=cores[i])
    root.update_idletasks()

def gerar_dados():
    global dados
    dados = [random.randint(10, HEIGHT) for _ in range(NUM_BARRAS)]
    desenhar_barras(canvas, dados, ["blue"] * len(dados))

def bubble_sort_passo(i=0, j=0):
    if i < len(dados):
        if j < len(dados) - i - 1:
            cores = ["blue"] * len(dados)
            cores[j] = "red"
            cores[j + 1] = "red"
            if dados[j] > dados[j + 1]:
                dados[j], dados[j + 1] = dados[j + 1], dados[j]
            desenhar_barras(canvas, dados, cores)
            root.after(DELAY, lambda: bubble_sort_passo(i, j + 1))
        else:
            root.after(DELAY, lambda: bubble_sort_passo(i + 1, 0))
    else:
        desenhar_barras(canvas, dados, ["green"] * len(dados))


root = tk.Tk()
root.title("Simulador de Ordenação Visual - Bubble Sort")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack(pady=20)

frame = tk.Frame(root)
frame.pack()

btn_gerar = tk.Button(frame, text="Gerar Dados", command=gerar_dados)
btn_gerar.pack(side="left", padx=10)

btn_ordenar = tk.Button(frame, text="Iniciar Ordenação", command=lambda: bubble_sort_passo())
btn_ordenar.pack(side="left", padx=10)

gerar_dados()
root.mainloop()