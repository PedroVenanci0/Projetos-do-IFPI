# 6. Escreva um algoritmo para determinar o número de dígitos de um número informado.

def main():

    casas = 1
    ordem = 10

    numero = int(input('Informe um número: '))

    while (numero >= ordem):

        ordem *= 10 

        casas += 1
    
    print (f'Numero de dígitos igual a {casas}')
            
main()