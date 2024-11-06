# 25. Em uma eleição presidencial existem 3 (três) candidatos. Os votos são informados através de códigos.
# Os dados utilizados para a contagem dos votos obedecem à seguinte codificação:
# · 1, 2, 3 = voto para os respectivos candidatos;
# · 9 = voto nulo;
# · 0 = voto em branco;
# Escreva um algoritmo que leia o código votado por N eleitores. Ao final, calcule e escreva:
# a) total de votos para cada candidato;
# b) total de votos nulos;
# c) total de votos em branco;
# d) quem venceu a eleição.

def main():
    print ('\n>>>>>>>>>>> ELEIÇÕES ADS MURAL <<<<<<<<<<<')
    print ('==========================================\n')
    print('''       
· 1, 2, 3 = voto para os respectivos candidatos
· 9 = voto nulo
· 0 = voto em branco
''')
    
    candidato_01 = 0
    candidato_02 = 0
    candidato_03 = 0
    nulo = 0
    voto_branco = 0

    numero_eleitores = int(input("Informe o número de eleitores: "))

    contador = 1

    while contador <= numero_eleitores:

        opcao_voto = int(input('\nQual sua opção de voto: '))

        while opcao_voto != 1 and opcao_voto != 2 and opcao_voto != 3 and opcao_voto != 9 and opcao_voto != 0:
            print("\nVOTO INVALIDO!! TENTE NOVAMENTE...")
            opcao_voto = int(input('\nQual sua opção de voto: '))

        if opcao_voto == 1:
            candidato_01 += 1
        
        elif opcao_voto == 2:     
            candidato_02 += 1
        
        elif opcao_voto == 3: 
            candidato_03 += 1 
        
        elif opcao_voto == 9: 
            nulo += 1
        
        elif opcao_voto == 0:
            voto_branco += 1
        
        contador += 1

    Vencedor = CalculandoVencedor(candidato_01,candidato_02,candidato_03,nulo,voto_branco)

    print(f'''
          
========================================================================
                >>>>> RESULTADO DAS ELEIÇÕES <<<<<
========================================================================
. NÚMERO DE ELEITORES >> {numero_eleitores}
========================================================================
. Número de votos >> Candidato 01               -----------> {candidato_01}
. Número de votos >> Candidato 02               -----------> {candidato_02}
. Número de votos >> Candidatos 03              -----------> {candidato_03}
. Número de votos >> Nulos                      -----------> {nulo}
. Número de votos >> brancos                    -----------> {voto_branco} 
=======================================================================
. {Vencedor}
=======================================================================
''')

def CalculandoVencedor(candidato_01, candidato_02,candidato_03,nulo,branco):

    if candidato_02 > candidato_01 and candidato_02 > candidato_03 and candidato_02 > nulo and candidato_02 > branco:

        return 'Candidato_02 é o VENCEDOR!!!'

    elif candidato_03 > candidato_01 and candidato_03 > candidato_02 and candidato_03 > nulo and candidato_03 > branco:

        return 'Candidato_03 é o VENCEDOR!!!'

    elif branco > candidato_01 and branco > candidato_03 and branco > nulo and branco > candidato_02:
        return 'MUITOS VOTOS EM BRANCO! VOTAÇÃO ADIADA'

    elif nulo > candidato_01 and nulo > candidato_03 and nulo > candidato_02 and nulo > branco:
        return 'MUITOS VOTOS NULOS! VOTAÇÃO ADIADA'
    
    elif candidato_01 > candidato_02 and candidato_01 > candidato_03 and candidato_01 > nulo and candidato_01 > branco:

        return 'Candidato_01 é o VENCEDOR!!!'

    else: 
        return "NÚMERO DE VOTOS FOI O MESMO EM ALGUMAS CATEGORIAS!! VOTAÇÃO ADIADA !!"
main()