def criptografar(mensagem):
    # Primeira passagem: deslocar letras (minúsculas e maiúsculas) 3 posições para a direita
    mensagem_1 = []
    for char in mensagem:
        if 'a' <= char <= 'z':  # Se o caractere for minúscula
            mensagem_1.append(chr((ord(char) - ord('a') + 3) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':  # Se o caractere for maiúscula
            mensagem_1.append(chr((ord(char) - ord('A') + 3) % 26 + ord('A')))
        else:
            mensagem_1.append(char)  # Não altera caracteres não alfabéticos

    # Segunda passagem: inverter a string
    mensagem_2 = ''.join(mensagem_1)[::-1]

    # Terceira passagem: deslocar caracteres da metade para a esquerda
    metade = len(mensagem_2) // 2
    mensagem_3 = list(mensagem_2)

    for i in range(metade, len(mensagem_2)):
        if 'a' <= mensagem_3[i] <= 'z':  # Se o caractere for minúscula
            mensagem_3[i] = chr((ord(mensagem_3[i]) - ord('a') - 1) % 26 + ord('a'))
        elif 'A' <= mensagem_3[i] <= 'Z':  # Se o caractere for maiúscula
            mensagem_3[i] = chr((ord(mensagem_3[i]) - ord('A') - 1) % 26 + ord('A'))
        # Caracteres não alfabéticos (como '\', '{', '-') não são modificados

    return ''.join(mensagem_3)

def main():
    # Número de casos de teste
    N = int(input().strip())
    
    # Processa cada caso de teste
    for _ in range(N):
        mensagem = input().strip()
        print(criptografar(mensagem))

if __name__ == "__main__":
    main()
