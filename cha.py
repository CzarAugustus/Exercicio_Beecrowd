# Leitura do tipo de chá correto
T = int(input("Digite o tipo de chá correto (1 a 4): "))

# Leitura das respostas dos competidores
respostas = list(map(int, input("Digite as respostas dos competidores, separadas por espaço: ").split()))

# Contagem das respostas corretas
corretas = sum(1 for resposta in respostas if resposta == T)

# Exibindo o número de respostas corretas
print(corretas)
