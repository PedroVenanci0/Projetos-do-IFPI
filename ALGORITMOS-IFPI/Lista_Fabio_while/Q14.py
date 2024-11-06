# Emita o resultado de uma pesquisa de opinião pública a respeito das eleições presidenciais. O
# entrevistado deverá escolher entre 3 candidatos (Serra=45, Dilma=13 ou Ciro Gomes=23), ou então
# responder: indeciso=99, outros=98, nulo/branco=0. O algoritmo deve ler a opinião de voto de cada
# entrevistado, encerrando-se a pesquisa com a opinião sendo igual a –1. Ao final, devem ser mostrados:
# · a porcentagem de cada candidato;
# · a porcentagem dos outros candidatos;
# · a porcentagem de eleitores indecisos;
# · a porcentagem de votos nulos/brancos;
# · o total de entrevistados;
# · uma mensagem indicando a possibilidade ou não de haver 2o turno.



def main():

    print ('                                                  ----> PESQUISA DE OPINIÃO PÚBLICA <----                                                             ')
    print ('O entrevistado deverá escolher entre 3 candidatos (Serra=45, Dilma=13 ou Ciro Gomes=23), ou então responder: indeciso=99, outros=98, nulo/branco=0.')

    voto = ''
    total_de_entrevistados = 0
    contagem_voto_45 = 0
    contagem_voto_13 = 0
    contagem_voto_23 = 0
    contagem_voto_outros = 0
    contagem_voto_nulo = 0
    contagem_voto_indeciso = 0

    while voto != (-1):

        voto = int(input('Informe sua opção de voto: '))

        if (voto != (-1)):

            if voto == 45:

                contagem_voto_45 += 1
    
            elif voto == 13:

                contagem_voto_13 += 1
    
            elif voto == 23:

                contagem_voto_23 += 1
    
            elif voto == 98:
        
                contagem_voto_outros += 1
    
            elif voto == 0:

                contagem_voto_nulo += 1
    
            elif voto == 99:

                contagem_voto_indeciso += 1
    
            else:

                print ('VOTO inválido')
                total_de_entrevistados -= 2

        total_de_entrevistados += 1

        porcentagem_45 = (contagem_voto_45 / total_de_entrevistados) * 100    
        porcentagem_13 = (contagem_voto_13 / total_de_entrevistados) * 100    
        porcentagem_23 = (contagem_voto_23 / total_de_entrevistados) * 100    
        porcentagem_outros = (contagem_voto_outros / total_de_entrevistados) * 100    
        porcentagem_nulo = (contagem_voto_nulo / total_de_entrevistados) * 100    
        porcentagem_indeciso = (contagem_voto_indeciso / total_de_entrevistados) * 100 

    print (f'O total de entrevistados foi de {total_de_entrevistados} voluntarios')
    print (f'A porcentagem de votos do candidato (45) é de {porcentagem_45:.1f}%')
    print (f'A porcentagem de votos do candidato (13) é de {porcentagem_13:.1f}%')
    print (f'A porcentagem de votos do candidato (23) é de {porcentagem_23:.1f}%')
    print (f'A porcentagem de votos em outros candidatos foi de {porcentagem_outros:.1f}%')
    print (f'A porcentagem de votos nulos foi de {porcentagem_nulo:.1f}%')
    print (f'A porcentagem de votos indecisos foi de {porcentagem_indeciso:.1f}%')

    if porcentagem_45 > 50 or porcentagem_23 > 50 or porcentagem_13 > 50:

        print('Segundo as pesquisas, as eleicões seram vencidas no PRIMEIRO turno')
    else:
        print('Segundo as pesquisas, as eleicões seram vencidas no SEGUNDO turno')

       

    
    
main()