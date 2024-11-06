# 4. Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Geométrica que tem por valor inicial A0 e razão R.



def main():

    print (' ---->  PROGRESSÃO GEOMÉTRICA  <---- ')

    ValorInicial = int(input('Informe o valor inicial da progressão Geométrica: '))
    limite = int(input('Informe um valor limete para a progressão: '))
    razao = int(input('Informe a razão da progressão: '))

    ordem = ''

    for i in range(ValorInicial, limite):

        if ValorInicial < limite:

            ordem = ordem + str(ValorInicial) + ' '

        ValorInicial *= razao

    print (f'A ordem dos termos de sua PG é {ordem}')

main()