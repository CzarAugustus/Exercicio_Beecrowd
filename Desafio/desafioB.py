#def conta_diamante(d):
#    contador = 0
#    while '<>' in d:
#        contador += 1
#        d = d.replace('<>', '', 1)
#    return contador

#minerio = int(input())
#d = []
#for _ in range(minerio):
#    seq = input()
#    d.append(seq)

# Processando cada sequência de minério para contar os diamantes
#for sequencia in d:
#    resultado = conta_diamante(sequencia)
#    print(resultado)

# Recebe o número de casos de teste
#diamante = int(input())
#minerio = []

# Loop para cada caso de teste
#for _ in range(diamante):
#    entrada = input().strip()

    # Remove as partículas de areia
#    entrada = entrada.replace('.', '')

    # Inicializa a contagem de diamantes
#    contador = 0
#    lista = []

    # Percorre cada caractere na linha de entrada
 #   for char in entrada:
  #      if char == '<':
   #         # Adiciona o símbolo de abertura ao stack
    #        lista.append(char)
     #   elif char == '>' and lista:
      #      # Sempre que encontra um fechamento com um símbolo de abertura disponível
       #     lista.pop()
        #    contador += 1

    # Armazena o resultado de diamantes para este caso de teste
    #minerio.append(contador)

# Exibe os resultados
#for count in entrada:
 #   print(count)

def conta_diamante(d):
    contador = 0
    while '<>' in d:
        contador += 1
        d = d.replace('<>', '', 1)
    return contador

# Recebe o número de casos de teste
diamante = int(input())
minerio = []

# Loop para cada caso de teste
for _ in range(diamante):
    entrada = input().strip()

    # Remove as partículas de areia
    entrada = entrada.replace('.', '')

    # Conta os diamantes na entrada
    contador = conta_diamante(entrada)

    # Armazena o resultado de diamantes para este caso de teste
    minerio.append(contador)

# Exibe os resultados
for count in minerio:
    print(count)







