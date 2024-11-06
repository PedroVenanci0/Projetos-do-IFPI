# 23. Escreva um algoritmo que leia a razão de uma PG (Progressão Geométrica) e o seu primeiro termo e
# escreva os N termos da PG. Ler o valor de N.

def main():


    razão = int(input('Informe a razão da PG: '))
    termos_PG = int(input('Informe o primeiro termo da PG: '))
    numero_de_termos = int(input('Informe o numero de termos: '))

    contador = 0

    while contador < numero_de_termos:

        print (f'{termos_PG}')

        termos_PG = termos_PG * razão 

        contador += 1

main()