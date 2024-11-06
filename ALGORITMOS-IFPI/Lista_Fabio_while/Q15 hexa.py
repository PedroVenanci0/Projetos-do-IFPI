     
def main():

    print ('------> transformando decimal em binária e hexagonal <------')

    sair = 0
    binario = 0
    hexa = 0
    opcao = 1

   
    while opcao != 0:

        numero = limites_min_max('Qual o número: ', 1, 255)
        opcao = limites_min_max(menu(numero), 0, 3)

        if opcao == 2:
            binario = conversor_binario(numero)
            print(f'O número digitado foi {numero}. Em binário, ele corresponde a {binario}')

        elif opcao == 3: 
            hexa = conversor_hexa(numero)
            print(f'O número digitado foi {numero}. Em hexadecimal, ele corresponde a {hexa}')


    print('Encerrado!!')


     
def menu(numero):

    return f"""
    ---> CONVERSOR <---
  1 - Mudar Número - Atual: {numero}
  2 - Show in Binário
  3 - Show in Hexa
  
  0 - Encerrar
  >>>
    
    """

def conversor_binario(numero):
    
    ordem = ''

    while numero > 0:

        resto = numero % 2

        lista = (f'{resto}')

        numero //= 2

        ordem = str(lista) + ordem

    return ordem

def conversor_hexa(numero):

    ordem = ''

    while numero > 0:

        resto = numero % 16

        if resto < 10:
            ordem = str(resto) + ordem
        else:
            ordem = hexadecimal(resto) + ordem

        numero //= 16

    return ordem
    
def hexadecimal(resto):
    if resto == 10:
        return "A"
    
    elif resto == 11:
        return "B"
    
    elif resto == 12:
        return "C"
    
    elif resto == 13:
        return "D"
    
    elif resto == 14:
        return "E"
    
    elif resto == 15:
        return "F"

def limites_min_max(mensagem, min, max):
    numero = int(input(mensagem))
    if numero < min or numero > max:
        print('Número inválido! Digite novamente')
        return limites_min_max(mensagem, min, max)
    return numero

    

main()
