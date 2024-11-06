# 14. Leia N, calcule e escreva o maior quadrado menor ou igual a N. Por exemplo, se N for igual a 38, o
# maior quadrado menor que 38 é 36 (quadrado de 6).

def main():

    print("""
======================================
>>> DESCOBRINDO O Maior Quadrado <<<
======================================
""")

    maior_numero = 0

    numero_N = int(input('>> DIGITE UM VALOR PARA A COMPARAÇÃO: '))

    for contador in range(1, numero_N):
        valor = contador ** 2

        if valor <= numero_N:
            maior_numero = valor

            
    print (f'\n>> O maior quadrado menor ou igual a {numero_N} é {maior_numero}\n')



main()