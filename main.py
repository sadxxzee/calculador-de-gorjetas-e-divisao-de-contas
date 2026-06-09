import tkinter as tk

def calcular_total():
    total = float(campo_total.get())
    porcentagem = float(campo_porcentagem.get())
    compradores = float(campo_compradores.get())
    novoTotal = total * porcentagem /100 + total
    print(novoTotal)
    texto_resposta.config(text=novoTotal)
    valorindividual= novoTotal / compradores
    texto_valor_individual.config(text=valorindividual)


root = tk.Tk()
root.title("calculos de contas")
root.geometry("1200x800")

texto_total = tk.Label(root, text="insira o valor da sua conta : ")
texto_total.pack(pady=5)

campo_total = tk.Entry(root, width=30)
campo_total.pack(pady=10)

texto_porcentagem = tk.Label(root, text="insira a porcentagem do atendente : ")
texto_porcentagem.pack(pady=10)

campo_porcentagem = tk.Entry(root, width=30)
campo_porcentagem.pack(pady=10)

texto_compradores = tk.Label(root, text="insira em quantas pessoas vc ira dividir a conta : ")
texto_compradores.pack(pady=10)

campo_compradores = tk.Entry(root, width=30)
campo_compradores.pack(pady=10)

calculo_botao = tk.Button(root, text="Submit", command=(calcular_total))
calculo_botao.pack(pady=5)

texto_resposta = tk.Label(root, text="resposta : ")
texto_resposta.pack(pady=10)

texto_valor_individual = tk.Label(root, text="")
texto_valor_individual.pack(pady=10)
root.mainloop()