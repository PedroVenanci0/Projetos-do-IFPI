# 5. Leia um número, calcule e escreva seu fatorial.

def main():

    print(">> Calculando Fatoriais <<\n")

    numero = int(input('Informe um número: '))

    contagem = 1
    fatorial = 1

    while contagem <= numero:
        fatorial = fatorial * contagem
        contagem += 1
    print (f'{fatorial}')

main()