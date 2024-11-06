# 14. Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
# maior quadrado menor que 38 é 36 (quadrado de 6).


def main():

    print("""
======================================
>>> DESCOBRINDO O Maior Quadrado <<<
======================================
""")

    numero_n = int(input("Informe um número para a verificação: "))

    contador = 0
    maior_numero = 0

    while contador < numero_n:

        valor = contador ** 2
        contador += 1

        if valor <= numero_n:
            maior_numero = valor

    print (f'\n>> O maior quadrado menor ou igual a {(numero_n)} é {(maior_numero)}\n')

main()