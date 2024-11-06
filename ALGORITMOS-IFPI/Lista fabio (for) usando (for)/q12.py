# 12. Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

def main():

    somatorio = 0
    lista = ''
    media = 0
    ordem = ''

    tamanho_da_lista = int(input('Informe número de termos da Lista: '))

    for contador in range(1, tamanho_da_lista + 1):

        numero_N = float(input(f'\nInforme um {contador}° número: '))
        ordem += str(numero_N) + '\n'
        somatorio += numero_N

    media = somatorio / tamanho_da_lista

    
    print ('\n>>>> A lista de numeros <<<<\n')
    print (f'{ordem}')
    print (f'>>>>> O SOMATORIO DOS TERMOS É {somatorio}')
    print (f'>>>>> A MÉDIA DOS TERMOS É {media}')





    

main()