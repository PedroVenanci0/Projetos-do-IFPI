# 2. Leia N e escreva todos os números inteiros pares de 1 a N.

def main ():

    print(">> Lista de números Pares <<\n")

    numero = int(input('Informe o número inteiros: '))
    pares = 1

    while pares < numero:
        if pares % 2 == 0:
            print (f'{pares}')
        pares += 1

main()