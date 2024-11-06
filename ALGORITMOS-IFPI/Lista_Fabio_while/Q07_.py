# 7. Leia um número e, a seguir, leia uma lista de números até achar um igual ao primeiro número lido.

def main():

    numero = int(input('Informe um número: '))

    contador = 0

    while numero != contador:

        contador += 1

        lista = (f'{contador}')

        print (f'{lista}')
    
    print ('O número lido achou seu identico!!')


main()