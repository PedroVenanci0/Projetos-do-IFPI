# 5. Leia um número, calcule e escreva seu fatorial.

def main():

    print ('\n#####  CALCULANDO FATORIAL  #####')
    print ('---------------------------------\n')

    numero = int(input('Informe um número: '))

    valor_fatorial = 1

    for i in range(numero, 1, -1):

        valor_fatorial = valor_fatorial * i

    print (valor_fatorial)


main()