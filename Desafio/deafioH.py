while True:
    try:
        def copa_ou_duas_copas(numero_reclamacoes):
            """
            Determina se haverá uma ou duas Copas com base no número de reclamações.

            Args:
                numero_reclamacoes: Um número inteiro representando o número de reclamações.

            Returns:
                Uma string indicando se haverá uma ou duas Copas.
            """
            if numero_reclamacoes == 0:
                return "vai ter copa!"
            else:
                return "vai ter duas!"

        # Lê o número de reclamações
        reclamacoes = int(input())  # Lê o número de reclamações para cada caso

        # Processa o caso
        resultado = copa_ou_duas_copas(reclamacoes)
        print(resultado)  # Imprime o resultado imediatamente após processar a entrada

    except EOFError:
        break  # Encerra o loop quando o fim do arquivo (EOF) é alcançado
    except Exception as e:
        print(f"Erro inesperado: {e}")
        break  # Encerra em caso de erro inesperado
