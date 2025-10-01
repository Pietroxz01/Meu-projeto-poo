import tkinter as tk
import random

WIDTH = 800
HEIGHT = 400
NUM_BARRAS = 20
DELAY = 50

# Variável global para controlar a ordenação
ordenacao_ativa = False

def desenhar_barras(canvas, dados, cores):
    canvas.delete("all")
    largura = WIDTH / len(dados)
    for i, valor in enumerate(dados):
        x0 = i * largura
        y0 = HEIGHT - valor
        x1 = (i + 1) * largura
        y1 = HEIGHT 
        # Desenha a barra
        canvas.create_rectangle(x0, y0, x1, y1, fill=cores[i])
        # Adiciona o número (valor) acima da barra
        canvas.create_text(x0 + largura/2, y0 - 10, text=str(valor), font=("Arial", 8))
    root.update_idletasks()

def parar_ordenacao():
    global ordenacao_ativa
    ordenacao_ativa = False
    btn_ordenar.config(state="normal")
    btn_parar.config(state="disabled")

def gerar_dados():
    global dados, ordenacao_ativa
    # Para qualquer ordenação em andamento
    parar_ordenacao()
    
    dados = [random.randint(10, HEIGHT-30) for _ in range(NUM_BARRAS)]
    desenhar_barras(canvas, dados, ["red"] * len(dados))
    info_label.config(text=f"Número de elementos: {len(dados)} - Pronto para ordenar")

def bubble_sort_passo(i=0, j=0):
    global ordenacao_ativa
    
    # Se a ordenação foi parada, não continua
    if not ordenacao_ativa:
        return
        
    if i < len(dados):
        if j < len(dados) - i - 1:
            cores = ["purple"] * len(dados)
            cores[j] = "pink"
            cores[j + 1] = "pink"
            if dados[j] > dados[j + 1]:
                dados[j], dados[j + 1] = dados[j + 1], dados[j]
            desenhar_barras(canvas, dados, cores)
            info_label.config(text=f"Ordenando... Passo {i+1}.{j+1} - Comparando posições {j} e {j+1}")
            root.after(DELAY, lambda: bubble_sort_passo(i, j + 1))
        else:
            root.after(DELAY, lambda: bubble_sort_passo(i + 1, 0))
    else:
        desenhar_barras(canvas, dados, ["green"] * len(dados))
        info_label.config(text="Ordenação concluída!")
        ordenacao_ativa = False
        btn_ordenar.config(state="normal")
        btn_parar.config(state="disabled")

def iniciar_ordenacao():
    global ordenacao_ativa
    if not ordenacao_ativa:
        ordenacao_ativa = True
        btn_ordenar.config(state="disabled")
        btn_parar.config(state="normal")
        bubble_sort_passo()

# Versão alternativa com entrada manual de dados
def adicionar_dados_manuais():
    def processar_entrada():
        try:
            entrada = entry.get()
            # Converte string para lista de números
            novos_dados = [int(x.strip()) for x in entrada.split(",")]
            global dados
            dados = novos_dados
            parar_ordenacao()  # Para ordenação se estiver ativa
            desenhar_barras(canvas, dados, ["blue"] * len(dados))
            info_label.config(text=f"Número de elementos: {len(dados)} - Dados manuais carregados")
            janela_entrada.destroy()
        except ValueError:
            label_erro.config(text="Erro: Digite números válidos separados por vírgula!")

    janela_entrada = tk.Toplevel(root)
    janela_entrada.title("Adicionar Dados Manuais")
    janela_entrada.geometry("400x150")
    
    tk.Label(janela_entrada, text="Digite os números separados por vírgula:").pack(pady=10)
    entry = tk.Entry(janela_entrada, width=50)
    entry.pack(pady=5)
    entry.insert(0, ", ".join(map(str, dados)))  # Mostra dados atuais
    
    tk.Button(janela_entrada, text="Aplicar", command=processar_entrada).pack(pady=5)
    label_erro = tk.Label(janela_entrada, text="", fg="red")
    label_erro.pack()

# Interface principal
root = tk.Tk()
root.title("Simulador de Ordenação Visual - Bubble Sort")

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack(pady=20)

frame_botoes = tk.Frame(root)
frame_botoes.pack()

btn_gerar = tk.Button(frame_botoes, text="Gerar Dados Aleatórios", command=gerar_dados)
btn_gerar.pack(side="left", padx=5)

btn_manuais = tk.Button(frame_botoes, text="Dados Manuais", command=adicionar_dados_manuais)
btn_manuais.pack(side="left", padx=5)

btn_ordenar = tk.Button(frame_botoes, text="Iniciar Ordenação", command=iniciar_ordenacao)
btn_ordenar.pack(side="left", padx=5)

btn_parar = tk.Button(frame_botoes, text="Parar Ordenação", command=parar_ordenacao, state="disabled")
btn_parar.pack(side="left", padx=5)

# Label para mostrar informações
info_label = tk.Label(root, text=f"Número de elementos: {NUM_BARRAS} - Pronto para ordenar", font=("Arial", 10))
info_label.pack(pady=5)

# Inicialização
dados = [random.randint(10, HEIGHT-30) for _ in range(NUM_BARRAS)]
desenhar_barras(canvas, dados, ["red"] * len(dados))

root.mainloop()
