# 1. Leia N e escreva todos os números inteiros de 1 a N.

def main():

    print(">> Ordem de números <<\n")

    num = int(input('Informe um número inteiro: '))
    contagem = 0

    while contagem < num: 
        contagem += 1
        print (f'{contagem}')

main()