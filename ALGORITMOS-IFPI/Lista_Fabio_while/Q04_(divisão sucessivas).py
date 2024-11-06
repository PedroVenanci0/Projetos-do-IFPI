# 4. Leia um número e divida-o por dois (sucessivamente) até que o resultado seja menor que 1. Escreva o resultado da última divisão efetuada.

def main():

    # Entrada 

    numero = float(input('Informe um número: '))

    # processamento 

    resultado_da_divisao = dividindo(numero)

    # saida 

    print (resultado_da_divisao)

def dividindo(numero):

    while numero >= 1:

         numero /= 2

    return (numero)


main()