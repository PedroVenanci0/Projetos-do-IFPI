# Leia N, calcule e escreva o valor de S.

# (tabela)

def main():

    numero_N = int(input('Informe um valor: '))

    solucao = 0

    contador = 1

    while contador < numero_N + 1:

        solucao += (1 / contador)
        contador += 1
    
    print (solucao)

main()