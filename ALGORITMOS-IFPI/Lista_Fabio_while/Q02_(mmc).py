# 2. Leia 2 (dois) números, calcule e escreva o mmc (mínimo múltiplo comum) entre os números lidos.

def main():

    # Entrada 

    num_01 = int(input('informe o primeiro número: '))
    num_02 = int(input('Informe o segundo número: '))

    # Processamento 

    mmc = calculando_mmc(num_01, num_02)

    # saida 

    print (f'----> Primeiro Número: {num_01} <----')
    print (f'----> Segundo Número: {num_02}   <----')
    print (f'----> MMC dos Números: {mmc} <----')



def calculando_mmc(n1, n2):

    resultado = abs(n1 * n2) // mdc(n1, n2)

    return resultado

def mdc(n1, n2):
    
    while n2 != 0:

        n1, n2 = n2, n1 % n2

    return n1


main()