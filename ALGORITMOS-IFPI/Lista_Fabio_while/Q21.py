# 21. Leia 2 números inteiros e escreva a multiplicação dos mesmos, sem que o operador de multiplicação (*) seja utilizado.

def main():

    numero_01 = int(input('Informe o primeiro numero: '))
    numero_02 = int(input('Informe o segundo numero: '))

    numero_fixo = numero_01

    contador = 1

    while contador < numero_02:

        numero_01 += numero_fixo

        contador += 1
    
    print (numero_01)



main()