# 3. Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.


def main():

    print ('\n ---->  PROGRESSÃO ARITIMÉTICA  <---- \n')

    ValorInicial = int(input('Informe o valor inicial da progressão aritimética: '))
    limite = int(input('Informe um valor limete para a progressão: '))
    razao = int(input('Informe a razão da progressão: '))

    ordem = list(i for i in range(ValorInicial, limite, razao))
    
    print (f'A ordem dos termos da PA é {ordem}')

main()