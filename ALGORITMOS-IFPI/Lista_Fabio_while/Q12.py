# 12. Leia vários códigos do jogador (1 ou 2) que ganhou o ponto, em uma partida de pingue-pongue, e
# responda quem ganha a partida. A partida chega ao final se:

# · Um dos jogadores chega a 21 pontos e a diferença de pontos entre os jogadores é maior ou igual a 2.
# · Se a primeira não for atendida, ganha aquele que, com mais de 21 pontos, consiga colocar uma diferença de 2 pontos sobre o adversário.

def main():

    print ('------ JOGO DE PING PONG ONLINE ------')
    print ('------ DIGITE "1" PARA PONTO DO PLAYER 1 E "2" PARA PLAYER 2 ------')

    pontos_01 = 0
    pontos_02 = 0

    while ((pontos_01 < 7) or (pontos_02 < 7)):

        pontos = int(input('Informe de quem foi o ponto: '))

        if pontos == 1: 
            pontos_01 += 1
        
        elif pontos == 2:
            pontos_02 += 1
        
        else:
            print ('Número digitado invalido')
        
    if pontos_01 - 2 >= pontos_02:

        return ('PLAYER 01 VENCEU!!!')
    
    elif pontos_02 - 2 >= pontos_01:

        return ('PLAYER 02 VENCEU!!!')
    
    else:

        while (pontos_01 - pontos_02 < 2) and (pontos_02 - pontos_01 < 2):

            pontos = int(input('Informe de quem foi o ponto: '))

            if pontos == 1: 
                pontos_01 += 1
            elif pontos == 2:
                pontos_02 += 1
            else:
                return ('Número digitado invalido')
            
        if pontos_01 > pontos_02:

            return ('PLAYER 01 VENCEU!!!')
    
        else:
            return ('PLAYER 02 VENCEU!!!')


main()