A = float(input())
A = round(A, 1)
B = float(input())
B = round(B, 1)
C = float(input())
C = round(C, 1)


peso_A = 2
peso_B = 3
peso_C = 5

media = (A * peso_A + B * peso_B + C * peso_C) / (peso_A + peso_B + peso_C)

print("MEDIA = {:.1f}".format(media))