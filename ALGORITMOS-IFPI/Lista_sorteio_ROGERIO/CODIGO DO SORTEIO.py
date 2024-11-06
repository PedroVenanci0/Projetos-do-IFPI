import random

def main():


    opcao_do_usuario = int(input(menu()))



def menu():

    return """

    >>>>> SORTEANDO GRUPOS <<<<<

    1 > Selecione o numero de grupos <  ---------------->  voltar para menu e (armazenar lista de grupos)

    2 > Exibir Grupos ordenado por nome < (apresentar e editar a lista de grupos por nome e voltar para menu)

    3 > Gravar ultimo resultado em arquivo < caso tenho um arquivo modificado anteriormente, editar no arquivo.txt

    4 > Excluir alunos da lista, antes da criação dos grupos. (flag para parada (-1)) <   > Exibir lista de alunos, excluir da lista os selecionados para a seleção e voltar para menu
    
    5 > retornar algum aluno que foi exluido anteriormente
  
    0 - Encerrar
    >>>

       """


main()