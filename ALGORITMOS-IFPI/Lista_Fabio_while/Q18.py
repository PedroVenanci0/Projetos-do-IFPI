# 18. Supondo-se que a população de uma cidade A seja de 200.000 habitantes, com uma taxa anual de
# crescimento na ordem de 3.5%, e que a população de uma cidade B seja de 800.000 habitantes,
# crescendo a uma taxa anual de 1.35%, Escreva um algoritmo que determine quantos anos serão
# necessários, para que a população da cidade A ultrapasse a população da cidade B.

def main():

    cidade_A = 200000
    cidade_B = 800000
    anos = 0

    while cidade_A < cidade_B:

        anos += 1
        cidade_A = (cidade_A * 3.5/100) + cidade_A
        cidade_B = (cidade_B * 1.35/100) + cidade_B
        
    
    print (f'{anos}')

main()