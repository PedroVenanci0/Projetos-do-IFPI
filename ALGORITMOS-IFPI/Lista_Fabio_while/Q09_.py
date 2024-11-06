# 9. Confira o resultado de uma competição de natação entre dois clubes. O programa deve ler o número da
# prova e a quantidade de nadadores. O fim dos dados é indicado pelo número da prova igual a 0 e
# quantidade de nadadores igual a 0. A seguir, para cada nadador deverá ler nome, classificação, tempo,
# clube (“a” ou “b”) e determinar os pontos obtidos por cada clube, de acordo com o seguinte critério:

# Lugar Pontos
# 1            9
# 2            6
# 3            4
# 4            3

# Ao final, o algoritmo deve escreva os totais de pontos de cada clube, indicando o clube vencedor.

def main():

    numero_da_prova = int(input('Informe o número da prova: '))
    numero_de_nadadores = int(input('Informe o número de nadadores: '))

    pontos_a = 0
    pontos_b = 0


    while numero_da_prova != 0 or numero_de_nadadores != 0:

        while numero_de_nadadores != 0:

            nome = input('Qual o nome do nadador: ')
            classificação = int(input('Qual é a sua classificação: '))
            tempo = float(input('Qual é o seu tempo: '))
            clube = input('Qual é o seu clube ["a" ou "b"]: ')

            pontos = pontos_por_classificação(classificação)

            if clube == "a":

                pontos_a += pontos

            else:

                pontos_b += pontos

            numero_de_nadadores -= 1

        numero_da_prova = int(input('Informe o número da prova: '))
        numero_de_nadadores = int(input('Informe o número de nadadores: '))
    
    print(f'O CLUBE "A" TERMINOU COM: {pontos_a}')
    print(f'O CLUBE "B" TERMINOU COM: {pontos_b}')

    if pontos_a > pontos_b:
        print('O CLUBE "A" é o VENCEDOR!!')
    elif pontos_b > pontos_a:
        print('O CLUBE "B" é o VENCEDOR!!')
    else:
         print('OCORREU UM EMPATE!!')

        

def pontos_por_classificação(classificação):

    if classificação == 1:

        return 9
    
    elif classificação == 2:

        return 6
    
    elif classificação == 3:

        return 4
    
    elif classificação == 4:

        return 3

main()
