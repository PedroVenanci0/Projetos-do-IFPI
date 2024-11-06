from utils import clear_screen
import funcionalidade_utils as func_utils
import utils

Colunas_de_dados = {
    "escolas": 1,
    "cidades": 2,
    "estados": 3,
    "rede": 4,
    "renda": 6,
    "mediageral": 7,
    "linguagens": 8,
    "matematica": 9,
    "humanas": 10,
    "natureza": 11,
    "redacao": 12
}

def top_brasil(matriz):
    try:
        numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))
    except ValueError:
        print("\nErro: Por favor, insira um número válido.")
        input("\npressione Enter para voltar ao menu...")
        menu()
    
    if numero_escolas >= len(matriz):
        numero_escolas = len(matriz)

    clear_screen()
    print(f"\n{utils.lightblue("----- Top")} {utils.lightblue(str(numero_escolas))} {utils.lightblue("Escolas do Brasil -----")} \n")

    lista_melhores = []

    for i in range(numero_escolas):
        lista_melhores.append(matriz[i][Colunas_de_dados["escolas"]])

    for i in range(len(lista_melhores)):
        print(f"{utils.lightblue(str(i+1))} - {lista_melhores[i]}")

    input("\npressione Enter para voltar ao menu...")
    menu()


def top_brasil_area(matriz):

    clear_screen()
    print("""

> SELEÇÃO DE ÁREAS DICIPLINARES <
---------------------------------
1 - LINGUAGENS
2 - MATEMÁTICA
3 - CIÊNCIAS HUMANAS
4 - CIÊNCIAS DA NATUREZA
5 - REDAÇÃO
---------------------------------
""")

    try:
        opcao = int(input("Informe a área diciplicar para analise: "))
    except ValueError:
        print("\nErro: Por favor, insira um número válido.")
        input("\npressione Enter para voltar ao menu de Seleção...")
        top_brasil_area(matriz)

    match opcao:
        case 1:
            matriz_ordenada = func_utils.quick_sort(matriz,Colunas_de_dados["linguagens"])
            area_diciplinar = "LINGUAGENS"
        case 2:
            matriz_ordenada = func_utils.quick_sort(matriz,Colunas_de_dados["matematica"])
            area_diciplinar = "MATEMATICA"
        case 3:
            matriz_ordenada = func_utils.quick_sort(matriz,Colunas_de_dados["humanas"])
            area_diciplinar = "HUMANAS"
        case 4:
            matriz_ordenada = func_utils.quick_sort(matriz,Colunas_de_dados["natureza"])
            area_diciplinar = "NATUREZA"
        case 5:
            matriz_ordenada = func_utils.quick_sort(matriz,Colunas_de_dados["redacao"])
            area_diciplinar = "REDAÇÃO"
        case _:
            print("\nErro: Por favor, insira um número válido.")
            input("\npressione Enter para voltar ao menu de Seleção...")
            top_brasil_area(matriz)            
    
    numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))

    print(f"\n> MELHORES ESCOLAS EM {area_diciplinar} <")
    print("-------------------------------------\n")
    for i in range(numero_escolas):
        print(f"{i+1} - {matriz_ordenada[i][Colunas_de_dados['escolas']]}")
    
    input("\npressione Enter para voltar ao menu de Seleção...")
    menu()


def top_estado(matriz):

    clear_screen()

    print("> OS MELHORES DO ESTADO <")
    print("-------------------------")

    lista_regioes = ["CE", "PI", "BA", "PE", "RN", "SE", "MA", "PB", "AL", "AM", "PA", "RO", "RR", "AP", "TO", "SP", "RJ", "ES", "MG", "PR", "SC", "RS", "MT", "GO", "DF", "MG"]
    matriz_escolas = []
    estado_analisado = input("\nInforme a Sigla do estado a ser analisado: ").upper()

    if estado_analisado not in lista_regioes:
        print("\nErro: Por favor, insira uma Sigla válida.")
        input("\npressione Enter para voltar ao menu de Seleção...")
        top_estado(matriz)

    for i in range(len(matriz)):
        if str(matriz[i][Colunas_de_dados["estados"]]) == estado_analisado:
            matriz_escolas.append(matriz[i])
    

    matriz_ordenada = func_utils.quick_sort(matriz_escolas,Colunas_de_dados["mediageral"])

    numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))

    print(f"\n> MELHORES ESCOLAS DE {estado_analisado} <")
    print("-------------------------------------\n")
    for i in range(numero_escolas):
        print(f"{i+1} - {matriz_ordenada[i][Colunas_de_dados['escolas']]}")
    
    input("\npressione Enter para voltar ao menu de Seleção...")
    menu()

def top_estado_publica_privada(matriz):

    clear_screen()
    lista_regioes = ["CE", "PI", "BA", "PE", "RN", "SE", "MA", "PB", "AL", "AM", "PA", "RO", "RR", "AP", "TO", "SP", "RJ", "ES", "MG", "PR", "SC", "RS", "MT", "GO", "DF", "MG"]
    matriz_escolas = []
    print("> OS MELHORES DA REDE DICIPLINAR <")
    print("----------------------------------")

    estado_analisado = input("\nInforme a Sigla do estado a ser analisada: ").upper()

    if estado_analisado not in lista_regioes:
        print("\nErro: Por favor, insira uma Sigla válida.")
        input("\npressione Enter para voltar ao menu de Seleção...")
        top_estado_publica_privada(matriz)

    for i in range(len(matriz)):
        if matriz[i][Colunas_de_dados["estados"]] == estado_analisado:
            matriz_escolas.append(matriz[i])

    print("\n> Informe uma rede escolar <\n")

    try:
        rede_analisada = int(input("(1) - Municipal | (2) - Federal | (3) - Federal | (4) - Privada:\n\n> "))
    except ValueError:
        print("\nErro: Por favor, insira um número válido.")
        input("\npressione Enter para voltar ao menu de Seleção...")
        top_estado_publica_privada(matriz)

    match rede_analisada:
        case 1:
            rede_escolar = "Municipal"
        case 2:
            rede_escolar = "Estadual"
        case 3:
            rede_escolar = "Federal"
        case 4:
            rede_escolar = "Privada"
        case _:
            print("\nErro: Por favor, insira um número válido.")
            input("\npressione Enter para voltar ao menu de Seleção...")
            top_estado_publica_privada(matriz)

    matriz_rede = []
    
    for i in range(len(matriz_escolas)):
        if matriz_escolas[i][Colunas_de_dados["rede"]] == rede_escolar:
            matriz_rede.append(matriz_escolas[i])

    matriz_rede = func_utils.quick_sort(matriz_rede,Colunas_de_dados["mediageral"])

    try:
        numero_escolas = int(input("\nInforme o número de escolas a serem classficadas: "))
    except ValueError:
        print("\nErro: Por favor, insira um número válido.")
        input("\npressione Enter para voltar ao menu de Seleção...")
        top_estado_publica_privada(matriz)

    if numero_escolas > len(matriz_rede):
        numero_escolas = len(matriz_rede)

    print(f"\n> MELHORES ESCOLAS DA REDE {(rede_escolar).upper()} <")
    print("-------------------------------------\n")
    for i in range(numero_escolas):
       print(f"{i+1} - {matriz_rede[i][Colunas_de_dados['escolas']]}")
    
    input("\npressione Enter para voltar ao menu de Seleção...")
    menu()
    
def media_nacional(matriz):
    clear_screen()
    print("""

> ÁREA DICIPLINARES <
---------------------
1 - LINGUAGENS
2 - MATEMÁTICA
3 - CIÊNCIAS HUMANAS
4 - CIÊNCIAS DA NATUREZA
5 - REDAÇÃO
---------------------
""")

    try:
        opcao = int(input("Informe a área diciplicar para analise: "))
    except ValueError:
        print("\nErro: Por favor, insira um número válido.")
        media_nacional(matriz)

    match opcao:

        case 1:
            media = func_utils.media_nacional_area(matriz,Colunas_de_dados["linguagens"])
        case 2:
            media = func_utils.media_nacional_area(matriz,Colunas_de_dados["matematica"])
        case 3:
            media = func_utils.media_nacional_area(matriz,Colunas_de_dados["humanas"])
        case 4:
            media = func_utils.media_nacional_area(matriz,Colunas_de_dados["natureza"])
        case 5:
            media = func_utils.media_nacional_area(matriz,Colunas_de_dados["redacao"])
        case _:
            media_nacional(matriz)
    
    print(f"\nA media Nacional de pontos da área diciplinar escolhida é {utils.lightblue(f'{media:.2f}')}")
    input("\npressione Enter para voltar ao menu de Seleção...")
    menu()
        

def melhor_escola(matriz):
    clear_screen()
    print("""
> Seleção para Paremetro de analise <
-------------------------------------
1 - Area Diciplinar
2 - Estadual
3 - Nacional
-------------------------------------
""")

    try:
        opcao = int(input("Informe o Paremetro de analise para analise: "))
    except ValueError:
        print("\nErro: Por favor, insira um número válido.")
        input("\npressione Enter para voltar ao menu de Seleção...")
        melhor_escola(matriz)

    match opcao:
        case 1:
            func_utils.melhor_escola_area(matriz)
            menu()
        case 2:
            func_utils.melhor_escola_estadual(matriz)
            menu()
        case 3:
            func_utils.melhor_escola_nacional(matriz,Colunas_de_dados["mediageral"])
            menu()
        case _:
            melhor_escola(matriz)


def lista_escolas_estado_renda(matriz):
    clear_screen()
    print("> Lista de escolas com renda baixa <")
    print("------------------------------------")
    matriz_ordenada = func_utils.quick_sort_renda(matriz, Colunas_de_dados["renda"])

    estado_analisado = input("\nInforme o estado a ser analisado: ").upper()
    lista_escolas = []
    lista_rendas = []

    for i in range(len(matriz_ordenada)):
        if matriz_ordenada[i][Colunas_de_dados["estados"]] == estado_analisado:
            escola = matriz_ordenada[i][Colunas_de_dados["escolas"]]
            lista_escolas.append(escola)
            renda = matriz_ordenada[i][Colunas_de_dados["renda"]]
            lista_rendas.append(renda)

    print(f"> Escolas do {estado_analisado} ordenadas por renda <")
    for i in range(len(lista_escolas)):
        print(f"{i+1} - {lista_escolas[i]:^5} >>> {lista_rendas[i]}")

def escola_por_nome(matriz):
    clear_screen()
    print("> Pesquisa por Nome da Escola <")
    print("-------------------------------")
    try:
        nome_procurado = input("\nInforme o nome da escola: ").upper()
    except ValueError:
        print("\nErro: Por favor, insira um nome válido.")
        input("\npressione Enter para voltar ao menu de Seleção...")
        escola_por_nome(matriz)

    for i in range(len(matriz)):
        if matriz[i][Colunas_de_dados["escolas"]] == nome_procurado:
            print(f"""
{matriz[i][Colunas_de_dados['escolas']]}
----------------------------------------
Estado: {matriz[i][Colunas_de_dados['estados']]}
Media Geral: {matriz[i][Colunas_de_dados['mediageral']]}
Rede Escolar: {matriz[i][Colunas_de_dados['rede']]}
Renda:{matriz[i][Colunas_de_dados['renda']]}
""")    
            break
        else:
            print("\nNome nao encontrado, tente novamente!!")
            input("\npressione Enter para voltar ao menu de Seleção...")
            escola_por_nome(matriz)
    
    input("\npressione Enter para voltar ao menu...")
    menu()
    

def ranking_por_estado(matriz):
    clear_screen()
    print("> Melhores do Estado <")
    print("----------------------")
    try:
        estado_analisado = input("\nInforme a sigla do estado: ").upper()
    except ValueError:
        print("\nErro: Por favor, insira uma Sigla válida.")
        input("\npressione Enter para voltar ao menu de Seleção...")
        ranking_por_estado(matriz)

    contador = 0

    for i in range(len(matriz)):
        if matriz[i][Colunas_de_dados["estados"]] == estado_analisado:
            contador += 1
            print(f"""
{contador}° - {matriz[i][Colunas_de_dados['escolas']]}
----------------------------------------
Estado: {matriz[i][Colunas_de_dados['estados']]}
Media Geral: {matriz[i][Colunas_de_dados['mediageral']]}
Rede Escolar: {matriz[i][Colunas_de_dados['rede']]}
Renda:{matriz[i][Colunas_de_dados['renda']]}
""")        
        
    input("\npressione Enter para voltar ao menu...")
    menu()
            
def ranking_por_regiao(matriz):
    clear_screen()
    print("> Melhores do Região <")
    print("----------------------")
    try:
        regiao_analisada = input("Informe o nome da regiao: ").upper()
    except ValueError:
        print("\nErro: Por favor, insira  o nome da região válido.")
        input("\npressione Enter para voltar ao menu de Seleção...")
        ranking_por_regiao(matriz)

    contador = 0

    lista_nordeste = ["CE", "PI", "BA", "PE", "RN", "SE", "MA", "PB", "AL"]
    lista_norte = ["AM", "PA", "RO", "RR", "AP", "TO"]
    lista_sudeste = ["SP", "RJ", "ES", "MG"]
    lista_sul = ["PR", "SC", "RS"]
    lista_centro = ["MT", "GO", "DF", "MG"]

    dicionario_regiao = {
        "NORDESTE": lista_nordeste,
        "NORTE": lista_norte,
        "SUDESTE": lista_sudeste,
        "SUL": lista_sul,
        "CENTRO-OESTE": lista_centro
    }

    for i in range(len(matriz)):
        if matriz[i][Colunas_de_dados["estados"]] in dicionario_regiao[regiao_analisada]:
            contador += 1
            print(f"""
{contador}° - {matriz[i][Colunas_de_dados['escolas']]}
----------------------------------------
Cidade: {matriz[i][Colunas_de_dados["estados"]]}
Media Geral: {matriz[i][Colunas_de_dados['mediageral']]}
Rede Escolar: {matriz[i][Colunas_de_dados['rede']]}
Renda:{matriz[i][Colunas_de_dados['renda']]}
""")
        
    input("\npressione Enter para voltar ao menu...")
    menu()

def menu():
    utils.clear_screen()
    matriz = ler_arquivo()
    print(f"""

    {utils.lightblue("> ENEM POR ESCOLA - 2014 <")} 
=====================================
            
       > Menu de Consulta <
{utils.lightblue("-------------------------------------")}
1 - Top N Brasil (todas as áreas)
2 - Top N Brasil por Área
3 - Top N por Estado
4 - Top N por Estado e Rede (pública ou privada)
5 - Media Nacional por Área
6 - Melhor escola por Área e Estado ou BR
7 - Listas Escolas por Estado Ordenada Por Renda
8 - Busca escola específica por parte  Nome
9 - Ranking ENEM por Estado
10 - Ranking ENEM por Região do País
          
0 - sair
{utils.lightblue("-------------------------------------")}
""")   
    
    try:
        opcao = int(input("> "))

    except ValueError:
        print("\nErro: Por favor, insira um número válido.")
        input("\nPressione Enter para voltar ao menu...")
        menu()

    match opcao:
        case 1:
            top_brasil(matriz)
        case 2:
            top_brasil_area(matriz)
        case 3:
            top_estado(matriz)
        case 4:
            top_estado_publica_privada(matriz)
        case 5:
            media_nacional(matriz)
        case 6:
            melhor_escola(matriz)
        case 7:
            lista_escolas_estado_renda(matriz)
        case 8:
            escola_por_nome(matriz)
        case 9:
            ranking_por_estado(matriz)
        case 10:
            ranking_por_regiao(matriz)
            pass
        case 0:
            print("fim...")
            return
        case _:
            print("\nInforme um número correspondente as opções!!!")
            input("\npressione Enter para voltar ao menu...")
            menu()

def ler_arquivo():

    arquivo = open("enem2014.txt.csv", encoding='cp1252')

    matriz = []

    for linha in arquivo:
        linha = linha.strip() 
        valores = linha.split(';')  
        matriz.append(valores) 
    
    return matriz