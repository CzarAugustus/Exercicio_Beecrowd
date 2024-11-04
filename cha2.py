def contar_acertos(tipo_real, respostas):
    return respostas.count(tipo_real)

# Lendo a entrada
tipo_real = int(input())
respostas = list(map(int, input().split()))

# Calculando o número de acertos
acertos = contar_acertos(tipo_real, respostas)

# Exibindo o resultado
print(acertos)
