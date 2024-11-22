def calcular_quadrado_matriz(matriz):
    return [[elemento ** 2 for elemento in linha] for linha in matriz]

def imprimir_matriz_formatada(matriz, numero_matriz):
    largura_maxima = max(len(str(num)) for linha in matriz for num in linha)
    
    print(f"Quadrado da matriz #{numero_matriz}:")
    
    for linha in matriz:
        print(" ".join(f"{num:>{largura_maxima}}" for num in linha))

def main():
    N = int(input().strip())
    
    for i in range(N):
        M = int(input().strip())
        
        matriz = []
        for _ in range(M):
            linha = list(map(int, input().strip().split()))
            matriz.append(linha)
        
        matriz_quadrada = calcular_quadrado_matriz(matriz)
        
        if i > 0:
            print()
        imprimir_matriz_formatada(matriz_quadrada, i + 4)

if __name__ == "__main__":
    main()
