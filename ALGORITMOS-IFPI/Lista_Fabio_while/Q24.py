# 24. Escreva um algoritmo que leia a razão de uma PA (Progressão Aritmética) e o seu primeiro termo e escreva os N termos da PA. Ler o valor de N.


def main():


    razão = int(input('Informe a razão da PA: '))
    termos_PA = int(input('Informe o primeiro termo da PA: '))
    numero_de_termos = int(input('Informe o numero de termos: '))

    contador = 0

    while contador < numero_de_termos:

        print (f'{termos_PA}')

        termos_PA = termos_PA + razão 

        contador += 1

main()