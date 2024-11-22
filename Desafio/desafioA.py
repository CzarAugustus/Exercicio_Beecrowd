def ordenar(numeros):
    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    pares.sort()
    impares.sort(reverse=True)

    return pares + impares

quantidade = int(input())
numeros = []
for i in range(quantidade):
    numero = int(input())
    numeros.append(numero)
#entrada = input("")
#numeros = list(map(int, entrada.split()))

resultado = ordenar(numeros)
for numero in resultado:
    print(numero)

