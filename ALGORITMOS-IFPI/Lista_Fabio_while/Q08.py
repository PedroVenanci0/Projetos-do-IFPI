# 8. Leia um numero X e, a seguir, leia e escreva uma lista de números com o término da lista ocorrendo quando a soma de dois números consecutivos da lista for igual a X.

def main():

    numero_x = float(input('Informe a codição de parada da lista: '))

    numero_list_penultimo = 0
    numero_lista_ultimo = 0
    soma = 0
    lista = ''

    while numero_x != soma:

        numero_lista = int(input('Informe um número: '))

        numero_list_penultimo = numero_lista_ultimo
        numero_lista_ultimo = numero_lista

        soma = numero_list_penultimo + numero_lista_ultimo

        lista += str(numero_lista_ultimo) + ' '

    
    print (f'[ {lista}]')
       
    
    
    



main()