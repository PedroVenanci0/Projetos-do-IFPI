def main():
    a,b,c = map(float,input().split())
    if a != 0:
        delta = (b**2) - (4*a*c)
        if delta > 0:
            raiz_delta = delta**0.5
            R1 = (- b + raiz_delta) / (2 * a)
            R2 = (- b - raiz_delta) / (2 * a)
            print(f'R1 = {R1:.5f}')
            print(f'R2 = {R2:.5f}')
        else:
            print('Impossivel calcular')
    else:
        print('Impossivel calcular')
main()