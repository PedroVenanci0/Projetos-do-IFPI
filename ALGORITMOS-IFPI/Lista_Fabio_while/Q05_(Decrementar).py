# Leia dois números X e N. A seguir, escreva o resultado das divisões de X por N onde, após cadadivisão, 
# X passa a ter como conteúdo o resultado da divisão anterior e N é decrementado de 1 em 1, até chegar a 2.

def main():

    # Entrada 

    numero_X = int(input('Inforne um valor para X: '))
    numero_N = int(input('Inforne um valor para N: '))

    while (numero_N != 2):

       numero_X = numero_X / numero_N

       print (f'X passou a ser {numero_X}')

       numero_N -= 1

       print (f'N foi decrementado em 1 e agora é {numero_N}')


main()