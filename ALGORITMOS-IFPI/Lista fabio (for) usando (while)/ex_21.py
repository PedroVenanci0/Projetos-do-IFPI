# Leia N, calcule e escreva o valor de S.

razao = 2
termo_inicial = 1

def main():
    
    numero_N = int(input('Digite um número: '))
    
    while numero_N == 0:
        
        print('Valor inválido!! Tente novamente.')
        numero_N = int(input('Digite um número: '))
    
    numerador = 1
    solucao = 0
    denominador = 1
        
    while denominador < numero_N + 1:
        
        solucao += numerador / denominador

        numerador += 2
        denominador += 1 
        
    print (solucao)
    

main()