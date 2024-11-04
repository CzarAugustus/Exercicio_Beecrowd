codigo_1, numero_1, valorUnit_1 = input().split()
codigo_1 = int(codigo_1)
numero_1 = int(numero_1)
valorUnit_1 = float(valorUnit_1)

codigo_2, numero_2, valorUnit_2 = input().split()
codigo_2 = int(codigo_2)
numero_2 = int(numero_2)
valorUnit_2 = float(valorUnit_2)

vTotal_peca_1 = numero_1 * valorUnit_1
vTotal_peca_2 = numero_2 * valorUnit_2
vTotal_pagar = vTotal_peca_1 + vTotal_peca_2

print(f"VALOR A PAGAR: R$ {vTotal_pagar:.2f}")


