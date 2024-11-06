import utils

Colunas_de_dados = {
    "escolas": 1,
    "cidades": 2,
    "estados": 3,
    "rede": 4,
    "renda": 5,
    "mediageral": 7,
    "linguagens": 8,
    "matematica": 9,
    "humanas": 10,
    "natureza": 11,
    "redacao": 12
}

def ler_arquivo():

    arquivo = open("enem2014.txt.csv", encoding='cp1252')

    matriz = []  # Cria a matriz (lista de listas)

    for linha in arquivo:
        linha = linha.strip() 
        valores = linha.split(';')  
        matriz.append(valores) 
    return matriz

matriz = ler_arquivo()


def quick_sort(matriz,key):

    if len(matriz) <= 1:
        return matriz

    pivot = matriz[len(matriz) // 2]
    left = []
    right = []

    for i in range(len(matriz)):
        if matriz[i][key] > pivot[key]:
            left.append(matriz[i])
        elif matriz[i][key] < pivot[key]:
            right.append(matriz[i])
    
    # Concatenando as listas corretamente
    return quick_sort(left,key) + [pivot] + quick_sort(right,key)

def quick_sort_renda(matriz, key):
    dicionario_renda = {
        'Muito Alto': 8,
        'Alto': 7,
        'M‚dio Alto': 6,
        'M‚dio': 5,
        'M‚dio Baixo': 4,
        'Baixo': 3,
        'Muito Baixo': 2,
        'Sem informa‡Æo':1
    }

    if len(matriz) <= 1:
        return matriz

    pivot = matriz[len(matriz) // 2]
    left = []
    right = []

    for i in range(len(matriz)):

        if dicionario_renda[matriz[i][key]] > dicionario_renda[pivot[key]]:
            left.append(matriz[i])
        elif dicionario_renda[matriz[i][key]] < dicionario_renda[pivot[key]]:
            right.append(matriz[i])
    
    return quick_sort_renda(left, key) + [pivot] + quick_sort_renda(right, key)

def media_nacional_area(matriz,key):
    lista_notas = []
    somatorio = 0

    for i in range(len(matriz)):
        nota_modificada = (matriz[i][key]).replace(",",".")
        nota_modificada = float(nota_modificada)
        lista_notas.append(nota_modificada)
        somatorio += nota_modificada

    qtd_notas = len(lista_notas)
    media = somatorio/qtd_notas
    return media 


def melhor_escola_area(matriz):
    utils.clear_screen()
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
        melhor_escola_area(matriz)

    match opcao:
        case 1:
            melhor_escola_diciplina(matriz,Colunas_de_dados["linguagens"])
        case 2:
            melhor_escola_diciplina(matriz,Colunas_de_dados["matematica"])
        case 3:
            melhor_escola_diciplina(matriz,Colunas_de_dados["humanas"])
        case 4:
            melhor_escola_diciplina(matriz,Colunas_de_dados["natureza"])
        case 5:
            melhor_escola_diciplina(matriz,Colunas_de_dados["redacao"])
        case _:
            melhor_escola_area(matriz)
        
def melhor_escola_diciplina(matriz,key):

    maior_nota = float(matriz[0][key].replace(",", "."))
    escola_atual = matriz[0][Colunas_de_dados["escolas"]]
    lista_repetidas = [escola_atual]

    for i in range(len(matriz)):
        nota_atual = float(matriz[i][key].replace(",", "."))
        
        if nota_atual > maior_nota:
            maior_nota = nota_atual  
            escola_atual = matriz[i][Colunas_de_dados["escolas"]]  
            lista_repetidas = [escola_atual] 

        elif nota_atual == maior_nota:
            escola_repetida = matriz[i][Colunas_de_dados["escolas"]]
            if escola_repetida != escola_atual:
                lista_repetidas.append(escola_repetida)

    if len(lista_repetidas) > 1:
        print(f"As melhores escolas em Linguagens com a maior nota são: ")
        for escola in lista_repetidas:
            print(f"- {escola}")
    else:
        print(f"\nA melhor escola na área de Linguagens é {escola_atual} com uma média de {utils.green(f"{maior_nota:.2f}")} pontos")
    
    input("\npressione Enter para voltar ao menu de Seleção...")
    



def melhor_escola_estadual(matriz):
    matriz_escolas = []
    estado_analisado = input("Informe o estado a ser analisado: ").upper()

    for i in range(len(matriz)):
        if str(matriz[i][Colunas_de_dados["estados"]]) == estado_analisado:
            matriz_escolas.append(matriz[i])

    matriz_ordenada = quick_sort(matriz_escolas,Colunas_de_dados["mediageral"])

    print(f"\nA melhor escola do estado {estado_analisado} é {utils.lightblue(matriz_ordenada[0][Colunas_de_dados['escolas']])}")
    input("\npressione Enter para voltar ao menu de Seleção...")

def melhor_escola_nacional(matriz,key):

    maior_nota = float(matriz[0][key].replace(",", "."))
    escola_atual = matriz[0][Colunas_de_dados["escolas"]]
    lista_repetidas = [escola_atual]

    for i in range(len(matriz)):
        nota_atual = float(matriz[i][key].replace(",", "."))
        
        if nota_atual > maior_nota:
            maior_nota = nota_atual  
            escola_atual = matriz[i][Colunas_de_dados["escolas"]]  
            lista_repetidas = [escola_atual] 

        elif nota_atual == maior_nota:
            escola_repetida = matriz[i][Colunas_de_dados["escolas"]]
            if escola_repetida != escola_atual:
                lista_repetidas.append(escola_repetida)

    if len(lista_repetidas) > 1:
        print(f"As melhores escolas nacionais com a mesma media geral são: ")
        for notas in lista_repetidas:
            print(f"- {notas}")
    else:
        print(f"\nA melhor escola nacional é {utils.lightblue(escola_atual)} com uma média geral de {maior_nota} pontos")
    
    input("\npressione Enter para voltar ao menu de Seleção...")



    