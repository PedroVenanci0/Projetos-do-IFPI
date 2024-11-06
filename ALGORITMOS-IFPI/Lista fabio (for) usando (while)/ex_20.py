# Leia N, calcule e escreva o valor de S.

def main():

    numero_N = int(input('Informe um valor: '))

    solucao = 0
    numerador = 1
    contador = 1

    while contador < numero_N + 1:

        solucao += (numerador / contador)
        contador += 1
    
    print (solucao)

main()