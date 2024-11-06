# 13. Leia N e uma lista de N números e escreva o maior número da lista.

from utils import clear_screen

def main():

    print("""
========================
   >> MAIOR NÚMERO <<
========================
""")

    tamanho_da_lista = int(input('>> Informe o tamanho da lista: '))

    numero = float(input('\n>> Digite um numero: '))

    maior_numero = numero

    lista = str(1) + "°" + " " + "-->" + " " + str(numero)

    for contador in range(1, tamanho_da_lista):

        numero = float(input('\n>> Digite um numero: '))

        contador += 1

        lista = lista + "\n" + str(contador) + "°" + " " + "-->" + " " + str(numero) 
    
        if numero > maior_numero:

            maior_numero = numero
        
    clear_screen()
        
    print ('\n>>>>> Lista de números <<<<<<\n')
    print (lista)
    print ('\n====================================================')
    print (f'O maior número dentre os digitados é {maior_numero}')
    print ('====================================================\n')





main()