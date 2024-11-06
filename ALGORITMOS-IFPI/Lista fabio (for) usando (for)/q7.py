# 7. Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

def main():
    print('\n===================================')
    print('>> Somatorio de números interios <<')
    print('===================================')

    numero_N = int(input('\nInforme um número: '))

    somatorio = 0

    for i in range(0, numero_N + 1 ):
        somatorio += i

    print ('\nA soma de todos os valores de 1 a 10 é',somatorio,"\n") 

main()