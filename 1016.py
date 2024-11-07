#x = 60
#y = 90
#Velocidade Relativa = y - x = 30km/h -> 30km/60min ou 0.5km/min
#tempo = distancia / velocidade
distanciaXY = int(input())
vel_relativa = 0.5
tempo = (distanciaXY / vel_relativa)

print(f"{tempo:.0f} minutos")

