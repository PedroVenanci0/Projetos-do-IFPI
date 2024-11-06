def main():
    numero_N = int(input(''))
    contador_testes = 0
    while contador_testes != numero_N:
        nota01, nota02, nota03 = map(float, input().split())
        media_ponderada = ((nota01 * 2) + (nota02 * 3) + (nota03 * 5)) / 10
        print (f'{media_ponderada:.1f}')
        contador_testes += 1
main()