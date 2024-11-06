# 15. Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).

def main():

    print("""
==================================
    >>> SEQUÊNCIA DE TERMOS <<<
==================================
""")

    numero_de_termos = int(input('Informe o número de termos: '))

    valor = 1

    ordem = ''

    sequencia = []

    for contador in range(2, numero_de_termos + 1):

        valor = valor + contador

        sequencia.append(str(valor))

    ordem = ', '.join(sequencia)

    print (f'\nA ordem de termos da sequência é (1, {ordem})\n')
main()