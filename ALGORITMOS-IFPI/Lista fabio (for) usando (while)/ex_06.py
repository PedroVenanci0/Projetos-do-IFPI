# 6. Escreva a tabuada dos números de 1 a 10.

def main():

    print ('----> TABUADA DO 1 AO 10 <-----\n')

    contador_total = 1
    contador_tabuada_1 = 1

    while contador_total <= 10:
        resultado = contador_total * contador_tabuada_1
        print (f'1 x {contador_total} = {resultado}')
        contador_total += 1 
main()