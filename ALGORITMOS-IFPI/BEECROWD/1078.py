def main():

    numero = int(input())

    contador_tabuada = 1

    while contador_tabuada <= 10:

        resultado = contador_tabuada * numero

        print (f'{contador_tabuada} x {numero} = {resultado}')

        contador_tabuada += 1

main()