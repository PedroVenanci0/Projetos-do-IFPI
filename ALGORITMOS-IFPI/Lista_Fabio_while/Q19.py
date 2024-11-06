# 19. Em um frigorífico, cada boi traz em seu pescoço um cartão contendo o seu n.o de identificação e seu
# peso. Escreva um algoritmo que leia um conjunto de cartões e escreva o n.o de identificação e o peso do
# boi mais magro e do boi mais gordo. (Flag: n.o identificação=0)

def main():

   

    numero_identificação = int(input('Informe o número de identificação: '))
    peso = float(input('Informe o peso do animal: '))

    numero_identificação_boi_pesado = numero_identificação
    numero_identificação_boi_leve = numero_identificação

    boi_mais_pesado = peso
    boi_mais_leve = peso

    while numero_identificação != 0:

        if peso > boi_mais_pesado:

            boi_mais_pesado = peso
            numero_identificação_boi_pesado = numero_identificação
        
        if peso < boi_mais_leve:

            boi_mais_leve = peso
            numero_identificação_boi_leve = numero_identificação
        
        numero_identificação = int(input('Informe o número de identificação: '))

        if (numero_identificação != 0):

            peso = float(input('Informe o peso do animal: '))
        
    
    print (f'O maior boi é o {numero_identificação_boi_pesado}° >>>> pesando um total de {boi_mais_pesado:.0f} kg ')
    print (f'O menor boi é o {numero_identificação_boi_leve}° >>>> pesando um total de {boi_mais_leve:.0f} kg ')



main()