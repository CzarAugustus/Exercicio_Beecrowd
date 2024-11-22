def main():
    testes = int(input())  # Lê o número de testes
    for _ in range(testes):
        enderecos, chaves = map(int, input().split())  # Lê o número de endereços e chaves
        listao = [[] for _ in range(enderecos)]  # Cria uma lista de listas para armazenar os valores
        ultimaColisao = [0] * enderecos  # Lista para controlar as colisões

        chaves_list = list(map(int, input().split()))  # Lê todas as chaves de uma vez e as converte em inteiros

        for tmp in chaves_list:
            tmp2 = tmp % enderecos  # Calcula a posição do endereço
            listao[tmp2].append(tmp)  # Adiciona a chave na lista de endereços
            ultimaColisao[tmp2] += 1  # Atualiza a contagem de colisões

        for x in range(enderecos):
            print(f"{x} ->", end=" ")
            for y in range(ultimaColisao[x]):
                print(f"{listao[x][y]} ->", end=" ")
            print("\\")
        
        if _ < testes - 1:
            print()  # Se não for o último teste, imprime uma linha em branco

if __name__ == "__main__":
    main()
