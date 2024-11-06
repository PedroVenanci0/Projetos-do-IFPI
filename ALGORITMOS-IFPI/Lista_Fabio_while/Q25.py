# 25. Foi feita uma pesquisa de audiência de canal de TV em várias casas em Teresina, num certo dia. Para
# cada casa visitada, o entrevistado informou o número do canal (2, 4, 5, 7, 10) e o número de pessoas que
# estavam assistindo TV. Escreva um algoritmo que leia um número indeterminado de dados (terminando
# quando for lido um canal igual a zero) e calcule o percentual de audiência para cada emissora,
# mostrando ao final, o número de cada canal e sua respectiva audiência.


def main():

    print ('>>> Pesquisa de audiência de canal de TV <<<')

    contador_pessoas_total = 0
    numero_de_pessoas_02 = 0
    numero_de_pessoas_04 = 0
    numero_de_pessoas_05 = 0
    numero_de_pessoas_07 = 0
    numero_de_pessoas_10 = 0

    canal = int(input('O número do canal é '))
    numero_de_pessoas = int(input('O número de pessoas nos assistindo é '))

    while canal != 0:

        contador_pessoas_total += numero_de_pessoas 

        if canal == 2:

            numero_de_pessoas_02 += numero_de_pessoas
        
        elif canal == 4:

            numero_de_pessoas_04 += numero_de_pessoas
        
        elif canal == 5:

            numero_de_pessoas_05 += numero_de_pessoas
        
        elif canal == 7:

            numero_de_pessoas_07 += numero_de_pessoas
        
        elif canal == 10:

            numero_de_pessoas_10 += numero_de_pessoas
        
        if canal != 0:

            canal = int(input('O número do canal é '))

            if canal != 0: 
                numero_de_pessoas = int(input('O número de pessoas nos assistindo é '))

        else: 

            print('CANAL DIGITADO INCORRETAMENTE!!! TENTE NOVAMENTE...')
            canal = int(input('O número do canal é '))
            numero_de_pessoas = int(input('O número de pessoas nos assistindo é '))


    porcentagem_audiência_02 = (contador_pessoas_total * numero_de_pessoas_02) / 100
    porcentagem_audiência_04 = (contador_pessoas_total * numero_de_pessoas_04) / 100
    porcentagem_audiência_05 = (contador_pessoas_total * numero_de_pessoas_05) / 100
    porcentagem_audiência_07 = (contador_pessoas_total * numero_de_pessoas_07) / 100
    porcentagem_audiência_10 = (contador_pessoas_total * numero_de_pessoas_10) / 100
    

    print (f"""
           
        >>>>>> PORCENTAGEM DE AUDIÊNDIA DOS CANAIS DE TV EM TERESINA <<<<<<<<
           \n   
        >>> O CANAL (02) TEVE UMA AUDIÊNCIA DE {porcentagem_audiência_02} <<<
        >>> O CANAL (04) TEVE UMA AUDIÊNCIA DE {porcentagem_audiência_04} <<<
        >>> O CANAL (05) TEVE UMA AUDIÊNCIA DE {porcentagem_audiência_05} <<<
        >>> O CANAL (07) TEVE UMA AUDIÊNCIA DE {porcentagem_audiência_07} <<<
        >>> O CANAL (10) TEVE UMA AUDIÊNCIA DE {porcentagem_audiência_10} <<<
        
""")

            

        





main()