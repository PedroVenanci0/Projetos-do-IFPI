# 22. Leia 2 números inteiros e escreva o quociente e o resto da divisão dos mesmos, sem que os operadores de divisão (/ e %) sejam utilizados.

def main():

    numero_01 = int(input('Informe o primeiro numero: '))
    numero_02 = int(input('Informe o segundo numero: '))

    contador_maior = 0
    contador_de_verificação = 1
    contador_menor = 0

    if numero_01 > numero_02:

        while contador_de_verificação * numero_02 < numero_01:

            contador_maior * numero_02

            contador_maior += 1

            contador_de_verificação += 1
        
        resto_maior = numero_01 - (contador_maior * numero_02)

        print (f'>>> O resultado da divisão é {contador_maior} \n>>> resto {resto_maior}')
        
    if numero_01 < numero_02:

        contador_menor = 0
        resto_menor = numero_01

        print (f'------>  O resultado da divisão é {contador_menor} \n>>> O resto é {resto_menor}')
main()

