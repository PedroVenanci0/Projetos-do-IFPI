# Leia N, calcule e escreva o valor de S.

# (tabela)

def main():

    numero_N = int(input('Informe um valor: '))

    solucao = 0

    for contador in range(1, numero_N + 1):

        solucao += (1 / contador)
    
    print (solucao)

main()