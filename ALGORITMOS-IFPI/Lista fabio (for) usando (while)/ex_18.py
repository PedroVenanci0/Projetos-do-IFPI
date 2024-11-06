# Leia N, calcule e escreva o valor de S.

def main():

    numero_N = int(input('Informe um valor: '))

    solucao = 0

    contador_unitario = 0

    contador = 1

    while contador < numero_N + 1:

        if contador_unitario < numero_N:

            solucao += (contador / (numero_N - contador_unitario))

            contador_unitario += 1

        contador += 1
    
    print (solucao)

main()