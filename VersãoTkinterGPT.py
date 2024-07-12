import random
import string
import math
import tkinter as tk
from tkinter import messagebox, simpledialog

class Usuario:
    def __init__(self, root):
        self.nome = simpledialog.askstring("Nome", "Olá! Qual é seu nome:", parent=root)

class Apresentando(Usuario):
    def __init__(self, root):
        super().__init__(root)
        if self.nome:
            messagebox.showinfo("Bem-vindo", f"Olá {self.nome}, sou a inteligência artificial GMR, porém estou em desenvolvimento, então sou limitado. Aqui está um MENU INICIAL com algumas coisas que posso ajudar:")
            menu(root)

def calcular(root):
    try:
        num1 = float(simpledialog.askstring("Número 1", "Número 1:", parent=root))
        num2 = float(simpledialog.askstring("Número 2", "Número 2:", parent=root))
        operacao = simpledialog.askstring("Operação", "Selecione a operação (Adição, Subtração, Multiplicação, Divisão, Potência, Raiz Quadrada):", parent=root)

        operacoes = {
            "Adição": num1 + num2,
            "Subtração": num1 - num2,
            "Multiplicação": num1 * num2,
            "Divisão": "Erro: Divisão por zero!" if num2 == 0 else num1 / num2,
            "Potência": num1 ** num2,
            "Raiz Quadrada": "Erro: Raiz quadrada de número negativo!" if num1 < 0 else num1 ** 0.5
        }

        resultado = operacoes.get(operacao, "Operação inválida")
        messagebox.showinfo("Resultado", f"Resultado: {resultado}" if isinstance(resultado, (int, float)) else resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira números válidos.")

def converter_temperaturas(root):
    try:
        valor = float(simpledialog.askstring("Valor", "Valor:", parent=root))
        origem = simpledialog.askstring("Origem", "Origem (Celsius, Fahrenheit, Kelvin):", parent=root)
        destino = simpledialog.askstring("Destino", "Destino (Celsius, Fahrenheit, Kelvin):", parent=root)

        conversoes = {
            ("Celsius", "Fahrenheit"): (valor * 9/5) + 32,
            ("Fahrenheit", "Celsius"): (valor - 32) * 5/9,
            ("Celsius", "Kelvin"): valor + 273.15,
            ("Kelvin", "Celsius"): valor - 273.15,
            ("Fahrenheit", "Kelvin"): (valor - 32) * 5/9 + 273.15,
            ("Kelvin", "Fahrenheit"): (valor - 273.15) * 9/5 + 32,
        }

        resultado = conversoes.get((origem, destino), valor if origem == destino else "Conversão inválida")
        messagebox.showinfo("Resultado", f"Resultado: {resultado:.2f} {destino}" if isinstance(resultado, float) else resultado)

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor numérico válido.")

def formas_geometricas(root):
    try:
        forma = simpledialog.askstring("Forma", "Selecione a forma geométrica (Quadrado, Retângulo, Círculo, Triângulo):", parent=root)

        if forma == 'Quadrado':
            lado = float(simpledialog.askstring("Lado", "Lado:", parent=root))
            area = lado ** 2
            perimetro = 4 * lado
        elif forma == 'Retângulo':
            largura = float(simpledialog.askstring("Largura", "Largura:", parent=root))
            altura = float(simpledialog.askstring("Altura", "Altura:", parent=root))
            area = largura * altura
            perimetro = 2 * (largura + altura)
        elif forma == 'Círculo':
            raio = float(simpledialog.askstring("Raio", "Raio:", parent=root))
            area = math.pi * (raio ** 2)
            perimetro = 2 * math.pi * raio
        elif forma == 'Triângulo':
            base = float(simpledialog.askstring("Base", "Base:", parent=root))
            altura = float(simpledialog.askstring("Altura", "Altura:", parent=root))
            lado1 = float(simpledialog.askstring("Lado 1", "Lado 1:", parent=root))
            lado2 = float(simpledialog.askstring("Lado 2", "Lado 2:", parent=root))
            lado3 = float(simpledialog.askstring("Lado 3", "Lado 3:", parent=root))
            area = (base * altura) / 2
            perimetro = lado1 + lado2 + lado3
        else:
            messagebox.showerror("Erro", "Forma inválida.")
            return

        messagebox.showinfo("Resultado", f"Área: {area:.2f}, Perímetro: {perimetro:.2f}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def calcular_desconto(root):
    try:
        preco = float(simpledialog.askstring("Preço", "Preço do produto: R$", parent=root))
        percentual = float(simpledialog.askstring("Percentual", "Percentual de desconto: %", parent=root))

        desconto = preco * (percentual / 100)
        preco_final = preco - desconto

        messagebox.showinfo("Resultado", f"Desconto: R$ {desconto:.2f}, Preço final: R$ {preco_final:.2f}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def converter_moedas(root):
    try:
        valor = float(simpledialog.askstring("Valor", "Valor:", parent=root))
        taxa = float(simpledialog.askstring("Taxa", "Taxa de conversão:", parent=root))
        moeda = simpledialog.askstring("Moeda", "Moeda (USD, EUR, GBP, JPY):", parent=root)

        resultado = valor * taxa

        messagebox.showinfo("Resultado", f"Resultado: {resultado:.2f} {moeda}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

def gerar_senha(root):
    try:
        tamanho = int(simpledialog.askstring("Tamanho", "Tamanho da senha:", parent=root))
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

        messagebox.showinfo("Senha Gerada", f"Senha gerada: {senha}")

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um valor inteiro para o tamanho da senha.")

def menu(root):
    def on_button_click(action):
        action(root)

    menu_window = tk.Toplevel(root)
    menu_window.title("Menu")
    
    options = [
        ("Calculadora", calcular),
        ("Conversão de Temperaturas", converter_temperaturas),
        ("Formas Geométricas", formas_geometricas),
        ("Calcular Desconto", calcular_desconto),
        ("Conversão de Moedas", converter_moedas),
        ("Gerador de Senhas", gerar_senha)
    ]
    
    for option_text, action in options:
        button = tk.Button(menu_window, text=option_text, command=lambda act=action: on_button_click(act))
        button.pack(pady=5)
    
    exit_button = tk.Button(menu_window, text="Sair", command=menu_window.destroy)
    exit_button.pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    Apresentando(root)
    root.mainloop()
