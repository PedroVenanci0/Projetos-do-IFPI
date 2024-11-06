# 7. Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.

def main():

    numero_N = int(input('Informe um número N: '))

    somatorio = 0
    contador = 0

    while (contador <= numero_N):
        somatorio += contador
        contador += 1

    print (f'A soma dos números de 1 a {numero_N} é {somatorio}')
main()