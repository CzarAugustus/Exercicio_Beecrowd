import sys
from bisect import bisect_left, bisect_right

def process_cases():
    results = []
    data = sys.stdin.read().splitlines()

    idx = 0
    while idx < len(data):
        # Lê a linha e remove espaços em branco
        line = data[idx].strip()

        # Ignora linhas em branco
        if not line:
            idx += 1
            continue

        # Lê o intervalo de poder (IP) e o número de tentativas (M)
        IP, M = map(int, line.split())

        # Se IP e M forem 0, significa que a entrada terminou
        if IP == 0 and M == 0:
            break

        ginasio = []

        # Processa cada tentativa de colocar um analógimón
        for _ in range(M):
            idx += 1
            PC, NA = map(int, data[idx].strip().split())

            # ... (resto do código)

        # Armazena o número final de analógimons no ginásio
        results.append(str(len(ginasio)))

    # Imprime todos os resultados, cada um em uma linha
    print("\n".join(results))

# Chama a função para processar os casos
process_cases()