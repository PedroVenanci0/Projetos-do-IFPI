# 3. Leia 2 (dois) números, calcule e escreva o mdc (máximo divisor comum) entre os números lidos.


def main():

    # Entrada 

    num_01 = int(input('informe o primeiro número: '))
    num_02 = int(input('Informe o segundo número: '))

    # Processamento 

    mdc = calculando_mdc(num_01, num_02)

    # saida 

    print (f'----> Primeiro Número: {num_01} <----')
    print (f'----> Segundo Número: {num_02}   <----')
    print (f'----> MDC dos Números: {mdc} <----')



def calculando_mdc(n1, n2):
    
    while n2 != 0:

        n1, n2 = n2, n1 % n2

    return n1


main()