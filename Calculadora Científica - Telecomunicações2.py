import math

# Funções auxiliares para entrada
def get_float_input(prompt):
    """Função auxiliar para obter entrada numérica do usuário com validação."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Erro: Digite um número válido!")

def get_positive_float_input(prompt):
    """Função auxiliar para obter um número positivo."""
    while True:
        num = get_float_input(prompt)
        if num > 0:
            return num
        print("Erro: O número deve ser positivo!")

# Operações matemáticas básicas
def soma():
    num1 = get_float_input("Digite o primeiro número: ")
    num2 = get_float_input("Digite o segundo número: ")
    return num1 + num2

def subtracao():
    num1 = get_float_input("Digite o primeiro número: ")
    num2 = get_float_input("Digite o segundo número: ")
    return num1 - num2

def multiplicacao():
    num1 = get_float_input("Digite o primeiro número: ")
    num2 = get_float_input("Digite o segundo número: ")
    return num1 * num2

def divisao():
    num1 = get_float_input("Digite o primeiro número: ")
    num2 = get_float_input("Digite o segundo número: ")
    if num2 == 0:
        raise ValueError("Divisão por zero!")
    return num1 / num2

def potencia():
    num1 = get_float_input("Digite o primeiro número: ")
    num2 = get_float_input("Digite o segundo número: ")
    return num1 ** num2

# Operações matemáticas avançadas
def raiz_quadrada():
    num = get_positive_float_input("Digite o número para raiz quadrada: ")
    return math.sqrt(num)

def logaritmo():
    num = get_positive_float_input("Digite o número para logaritmo: ")
    return math.log(num)

def logaritmo_base_10():
    num = get_positive_float_input("Digite o número para logaritmo de base 10: ")
    return math.log10(num)

def seno():
    num = get_float_input("Digite o ângulo em radianos para seno: ")
    return math.sin(num)

def cosseno():
    num = get_float_input("Digite o ângulo em radianos para cosseno: ")
    return math.cos(num)

def tangente():
    num = get_float_input("Digite o ângulo em radianos para tangente: ")
    return math.tan(num)

# Operações específicas para telecomunicações
def db_para_linear():
    num = get_float_input("Digite o valor em dB: ")
    return 10 ** (num / 10)

def linear_para_db():
    num = get_positive_float_input("Digite o valor linear: ")
    return 10 * math.log10(num)

def atenuacao_sinal():
    distancia = get_positive_float_input("Digite a distância (km): ")
    perda_por_km = get_positive_float_input("Digite a perda por km (dB/km): ")
    return distancia * perda_por_km

def graus_para_radianos():
    graus = get_float_input("Digite o ângulo em graus: ")
    return math.radians(graus)

# Operações avançadas com escolha de função
def derivada():
    print("Escolha a função para calcular a derivada:")
    print("1. f(x) = x²")
    print("2. f(x) = sin(x)")
    print("3. f(x) = e^x")
    escolha_func = input("Digite o número da função (1-3): ")

    funcs = {
        "1": lambda x: x**2,
        "2": math.sin,
        "3": math.exp
    }
    if escolha_func not in funcs:
        raise ValueError("Função inválida!")
    
    func = funcs[escolha_func]
    x = get_float_input("Digite o valor de x para calcular a derivada: ")
    h = 1e-5
    derivada = (func(x + h) - func(x)) / h
    return derivada, x, escolha_func

def integral():
    print("Escolha a função para calcular a integral:")
    print("1. f(x) = x²")
    print("2. f(x) = sin(x)")
    print("3. f(x) = e^x")
    escolha_func = input("Digite o número da função (1-3): ")

    funcs = {
        "1": lambda x: x**2,
        "2": math.sin,
        "3": math.exp
    }
    if escolha_func not in funcs:
        raise ValueError("Função inválida!")

    func = funcs[escolha_func]
    a = get_float_input("Digite o limite inferior da integral: ")
    b = get_float_input("Digite o limite superior da integral: ")
    n = int(get_float_input("Digite o número de subdivisões: "))
    if n <= 0:
        raise ValueError("O número de subdivisões deve ser positivo!")
    h = (b - a) / n
    integral = 0.5 * (func(a) + func(b))
    for i in range(1, n):
        integral += func(a + i * h)
    integral *= h
    return integral, a, b, escolha_func

# Operações de onda
def velocidade_onda():
    f = get_positive_float_input("Digite a frequência (Hz): ")
    lambda_ = get_positive_float_input("Digite o comprimento de onda (m): ")
    return f * lambda_

def comprimento_onda():
    v = get_positive_float_input("Digite a velocidade da onda (m/s): ")
    f = get_positive_float_input("Digite a frequência (Hz): ")
    return v / f

def frequencia_onda():
    v = get_positive_float_input("Digite a velocidade da onda (m/s): ")
    lambda_ = get_positive_float_input("Digite o comprimento de onda (m): ")
    return v / lambda_

# Função principal da calculadora
def calculadora_telecom():
    operacoes = {
        "1": (soma, "Soma"),
        "2": (subtracao, "Subtração"),
        "3": (multiplicacao, "Multiplicação"),
        "4": (divisao, "Divisão"),
        "5": (potencia, "Potência"),
        "6": (raiz_quadrada, "Raiz Quadrada"),
        "7": (logaritmo, "Logaritmo"),
        "8": (logaritmo_base_10, "Logaritmo de Base 10"),
        "9": (seno, "Seno"),
        "10": (cosseno, "Cosseno"),
        "11": (tangente, "Tangente"),
        "12": (db_para_linear, "Conversão de dB para Linear"),
        "13": (linear_para_db, "Conversão de Linear para dB"),
        "14": (atenuacao_sinal, "Calcular Atenuação de Sinal"),
        "15": (graus_para_radianos, "Converter Graus para Radianos"),
        "16": (derivada, "Derivada"),
        "17": (integral, "Integral (Aproximação)"),
        "18": (velocidade_onda, "Calcular Velocidade da Onda (v = f * λ)"),
        "19": (comprimento_onda, "Calcular Comprimento de Onda (λ = v / f)"),
        "20": (frequencia_onda, "Calcular Frequência da Onda (f = v / λ)"),
        "21": (lambda x: None, "Sair")
    }

    while True:
        print("\n=== Calculadora para Telecomunicações ===")
        for key, (func, desc) in operacoes.items():
            print(f"{key}. {desc}")
        escolha = input("Escolha a operação (1-21): ")

        if escolha not in operacoes:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            func, desc = operacoes[escolha]
            if escolha == '16':
                resultado, x, func_num = func()
                func_names = {"1": "f(x) = x²", "2": "f(x) = sin(x)", "3": "f(x) = e^x"}
                print(f"Derivada aproximada de {func_names[func_num]} em x = {x} é: {resultado}")
            elif escolha == '17':
                resultado, a, b, func_num = func()
                func_names = {"1": "f(x) = x²", "2": "f(x) = sin(x)", "3": "f(x) = e^x"}
                print(f"Integral aproximada de {func_names[func_num]} de {a} a {b} é: {resultado}")
            elif escolha == '21':
                print("Saindo da calculadora. Até logo!")
                break
            else:
                resultado = func()
                if escolha in ['12', '13']:  # Adiciona unidades para conversões de dB
                    unidade = " (Linear)" if escolha == '12' else " (dB)"
                    print(f"Resultado{unidade}: {resultado}")
                elif escolha in ['14']:
                    print(f"Resultado: {resultado} dB")
                elif escolha in ['15']:
                    print(f"Resultado (radianos): {resultado}")
                elif escolha in ['18', '19', '20']:
                    unidade = " m/s" if escolha == '18' else " m" if escolha == '19' else " Hz"
                    print(f"Resultado: {resultado}{unidade}")
                else:
                    print(f"Resultado: {resultado}")
        except Exception as e:
            print(f"Erro: {e}. Tente novamente.")

if __name__ == "__main__":
    calculadora_telecom()
