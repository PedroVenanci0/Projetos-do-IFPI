# 1. Leia uma lista de números e que para cada número lido, escreva o próprio número e a relação de seus divisores. (flag número = 0).

def main():

    print ('----------------------------------------------------')
    print ('---> RELAÇÃO DE DIVISORES DE UM NÚMERO QUALQUER <---')
    print ('----------------------------------------------------')

    numero = int(input('Informe um número: '))

    while (numero != 0):

        contador = 1

        while (contador <= numero):

            if numero % contador == 0:

                lista = (f'{contador}')

                print (f'{lista}')

            contador += 1

        numero = int(input('Informe um número: '))


    print('FIM...')

main()