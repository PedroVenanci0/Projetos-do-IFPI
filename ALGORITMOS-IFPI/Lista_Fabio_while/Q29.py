# 28. Escreva um algoritmo que gere um número aleatório inteiro (utilize a função rand(): aleatorio = rand())
# e solicite um número ao usuário. O objetivo é que o usuário acerte o número gerado. Se o número
# digitado for menor que o gerado, escreva “Maior”, se for maior, escreva “Menor”, e solicite novamente
# um número ao usuário. Repita este processo ate que o usuário acerte o número gerado. Após isso,
# escreva em quantas tentativas o usuário acertou.

import random

def main(): 

    maximo = int(input('Informe um limite númerico para o Game: '))
    numero_aleatorio = random.randint(1, maximo)

    palpite = int(input('Dígite seu palpite: '))

    tentativas = 1

    while (palpite != numero_aleatorio):

        if palpite > numero_aleatorio:

            print ('O NÚMERO SECRETO É MENOR!!')
        
        elif palpite < numero_aleatorio:

            print ('O NÚMERO SECRETO É MAIOR!!')

        palpite = int(input('Dígite seu palpite: '))

        tentativas += 1
    
    print (f'PARABENS VC ACERTOU!!! SEU NÚMERO TENTATIVAS FOI {tentativas}.')
    

        

        




main()