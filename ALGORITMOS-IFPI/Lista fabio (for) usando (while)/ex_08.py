# 8. Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.

def main():

    numero_N = int(input('Informe um número para que vejamos seus multiplos: '))
    limite_inferior = int(input('Informe o limite inferor: '))
    limite_superior = int(input('Informe o limite inferor: '))

    contador = 1

    while numero_N * contador <= limite_inferior:
        
        if numero_N * contador >= limite_inferior:
            multiplo = numero_N * contador
            print  (f'{multiplo}')

        contador += 1
    
    while numero_N * contador <= limite_superior:
        multiplo = numero_N * contador
        print (f'{multiplo}')
        contador += 1

    

    
main()