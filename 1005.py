A = float(input())
A = round(A, 1)
B = float(input())
B = round(B, 1)

peso_A = 3.5
peso_B = 7.5

media = (A * peso_A + B * peso_B) / (peso_A + peso_B)

print("MEDIA = {:.5f}".format(media))