# 11. Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.

def main():

    limite_inferior = int(input('Infrome o limite inferior: '))
    limite_superior = int(input('Infrome o limite superior: '))

    ordem = ''

    while(limite_inferior <= limite_superior):
        
        if (limite_inferior % 2 != 0) and (limite_inferior % 3 != 0) and (limite_inferior % 5 != 0):
            ordem = ordem + str(limite_inferior) + ' '
        limite_inferior += 1
    
    print (ordem)

        


main()