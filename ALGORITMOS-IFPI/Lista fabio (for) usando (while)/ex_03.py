# 3. Leia as variáveis A0, Limite e R e escreva os valores menores que Limite gerados pela Progressão
# Aritmética que tem por valor inicial A0 e razão R.

def main():
    
    print ('------->  CALCULANDO A PROGERESSÃO ARITMÉTICA <------- \n')

    inicial_A0 = int(input('Informe o valor inicial: '))
    limite = int(input('Informe o limite: '))
    razao = int(input('Informe a razão da PA: '))

    ordem = ''

    while inicial_A0 < limite:
        inicial_A0 += razao
        ordem = ordem + str(inicial_A0 ) + ' '

    print (f'A ordem dos números é {ordem}')
main()