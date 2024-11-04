# Entrada do número de elementos na sequência
N = int(input("Digite o valor de N: "))

# Entrada da sequência de números
sequencia = []
for _ in range(N):
    sequencia.append(int(input("Digite 1 ou 2: ")))

# Inicialização das variáveis
atual = sequencia[0]
i = 1
consecutivos = 1  # Inicia em 1, pois o primeiro número é marcado

# Loop para contar os consecutivos alternados
while i < N:
    if atual == 1:
        # Encontrar o próximo 2
        for j in range(i, N):
            if sequencia[j] == 2:
                consecutivos += 1
                atual = 2
                i = j + 1
                break
        else:
            break  # Sai do loop se não encontrar mais 2
    else:
        # Encontrar o próximo 1
        for j in range(i, N):
            if sequencia[j] == 1:
                consecutivos += 1
                atual = 1
                i = j + 1
                break
        else:
            break  # Sai do loop se não encontrar mais 1

# Saída do resultado
print("Quantidade máxima de números que podem ser marcados:", consecutivos)
