def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def simplificador_fracionario(numerador, denominador):
    valor_mdc = mdc(numerador, denominador)
    return numerador // valor_mdc, denominador // valor_mdc

def operacoes(n1, d1, n2, d2, operador):
    if operador == '+':
        numerador = n1 * d2 + n2 * d1
        denominador = d1 * d2
    elif operador == '-':
        numerador = n1 * d2 - n2 * d1
        denominador = d1 * d2
    elif operador == '*':
        numerador = n1 * n2
        denominador = d1 * d2
    elif operador == '/':
        if d2 == 0:
            raise ValueError("Não existe divisão por zero!")
        numerador = n1 * d2
        denominador = d1 * n2
    else:
        raise ValueError("Operador inválido!")
   
    return numerador, denominador

def n_caso():
    N = int(input())
    #resultados = []

    for _ in range(N):
        entrada = input().strip()
        
        try:
            n1_d1, operador, n2_d2 = entrada.split()
            n1, d1 = map(int, n1_d1.split('/'))
            n2, d2 = map(int, n2_d2.split('/'))
        except ValueError:
            print("Erro na entrada! Formato esperado: 'n1/d1 operador n2/d2'.")
            continue

        if d1 == 0 or d2 == 0:
            print("Denominador não pode ser zero.")
            continue

        try:
            numerador, denominador = operacoes(n1, d1, n2, d2, operador)
            numerador_simplificado, denominador_simplificado = simplificador_fracionario(numerador, denominador)
            
            print(f"{numerador}/{denominador} = {numerador_simplificado}/{denominador_simplificado}") 
        except ValueError as ve: 
            print(f"Erro de formatação: {ve}") 
        except IndexError as ie: 
            print(f"Erro de índice: {ie}")

n_caso()
