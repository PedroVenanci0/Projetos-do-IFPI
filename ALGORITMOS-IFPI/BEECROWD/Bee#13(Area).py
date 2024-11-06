a = float(input(''))
b = float(input(''))
c = float(input(''))

pi = 3.14159

triangulo = (a * c) / 2
raio_circulo = pi * c**2
area_trapezio = (a + b) * c/2
area_quadrado = b**2
area_retangulo = a * b

print (f'TRIANGULO: {triangulo:.3f}')      
print (f'CIRCULO: {raio_circulo:.3f}')
print (f'TRAPEZIO: {area_trapezio:.3f}')
print (f'QUADRADO: {area_quadrado:.3f}')
print (f'RETANGULO: {area_retangulo:.3f}')