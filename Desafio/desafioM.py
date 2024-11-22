import re

def calcular_dificuldade(enunciado):
    # Usamos expressão regular para capturar apenas palavras válidas (a-z, A-Z, e um ponto no final)
    palavras = re.findall(r'[a-zA-Z]+', enunciado)
    
    # Se não houver palavras válidas, o comprimento médio será 0
    if not palavras:
        return 0
    
    # Calcular o comprimento total das palavras válidas
    soma_comprimentos = sum(len(palavra) for palavra in palavras)
    
    # Calcular a média
    comprimento_medio = soma_comprimentos // len(palavras)
    
    # Classificar com base no comprimento médio
    if comprimento_medio <= 3:
        return 250
    elif comprimento_medio <= 5:
        return 500
    else:
        return 1000

def main():
    try:
        while True:
            enunciado = input().strip()  # Lê uma linha de entrada
            # Imprime a dificuldade do problema com base no comprimento médio das palavras
            print(calcular_dificuldade(enunciado))
    except EOFError:
        pass  # Fim de entrada, encerra o loop

if __name__ == "__main__":
    main()
