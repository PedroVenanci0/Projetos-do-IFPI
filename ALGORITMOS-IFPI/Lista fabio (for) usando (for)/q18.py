# Leia N, calcule e escreva o valor de S.

def main():

    numero_N = int(input('Informe um valor: '))

    solucao = 0

    contador_unitario = 0

    for contador in range(1, numero_N + 1):

        solucao += (contador / (numero_N - contador_unitario))

        contador_unitario += 1
    
    print (solucao)

main()