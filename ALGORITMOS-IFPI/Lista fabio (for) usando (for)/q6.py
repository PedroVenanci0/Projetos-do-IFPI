# 6. Escreva a tabuada dos números de 1 a 10.

def main():

    print("\n>>> Tabuada do 1 ao 10 <<<")

    identificando_tabuada = int(input('\nDe qual número vc dedseja vizualizar a tabuada: '))

    if identificando_tabuada > 10 or identificando_tabuada < 1:

        print ('Número invalido!!!\n Selecione um número entre 1 e 10.')
        identificando_tabuada = int(input('\nDe qual número vc dedseja vizualizar a tabuada: '))

    print (f" \n-----> TABUDA DO NÚMERO {identificando_tabuada} <-----\n")

    for i in range(1, 11):

        valor = i * identificando_tabuada

        print (f". {i} x {identificando_tabuada} = {valor}")
    print('')
main()