tempo_gasto = int(input(''))
velocidade_media = int(input(''))

# Automovel rende 12km/l

distancia_percorrida = tempo_gasto * velocidade_media

litros_necessarios = distancia_percorrida / 12

print (f'{litros_necessarios:.3f}')