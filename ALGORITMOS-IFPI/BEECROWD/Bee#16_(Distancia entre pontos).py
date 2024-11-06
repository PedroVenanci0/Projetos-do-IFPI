x1, y1 = float(input('informe x1: ')), float(input('informe y1: '))
x2, y2 = float(input('informe x2: ')), float(input('informe y2: '))

import math

distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print (f'{distancia:.4f}')

