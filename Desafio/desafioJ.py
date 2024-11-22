def leds_necessarios(numero):
    # Mapeia a quantidade de LEDs necessários para cada dígito
    leds_por_digito = {
        '0': 6,
        '1': 2,
        '2': 5,
        '3': 5,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 3,
        '8': 7,
        '9': 6
    }
    
    # Soma os LEDs necessários para cada dígito do número
    total_leds = sum(leds_por_digito[digit] for digit in numero)
    return total_leds

def main():
    # Lê o número de casos de teste
    N = int(input())
    
    # Processa cada caso de teste
    for _ in range(N):
        numero = input().strip()  # Lê o número (em formato de string)
        resultado = leds_necessarios(numero)
        print(f"{resultado} leds")

if __name__ == "__main__":
    main()
