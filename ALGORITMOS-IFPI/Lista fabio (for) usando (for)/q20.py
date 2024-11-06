# Leia N, calcule e escreva o valor de S.

def main():

    numero_N = int(input('Informe um valor: '))

    solucao = 0

    numerador= 1

    for contador in range(1, numero_N + 1,):

        solucao += (numerador / contador)
    
    print (solucao)

main()