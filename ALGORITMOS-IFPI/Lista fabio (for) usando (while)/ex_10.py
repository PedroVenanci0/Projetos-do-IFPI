# 10. Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.

def main():

    limite_inferior = int(input('Informe o limite inferior: '))
    limite_superior = int(input('Informe o limite superior: '))

    contador = 0

    resultado = 0

    while (resultado + 1) < limite_superior:
        
        if (limite_inferior + contador) % 2 == 1:
           resultado = limite_inferior + contador
           print (resultado)
        
        contador += 1    



        

main()