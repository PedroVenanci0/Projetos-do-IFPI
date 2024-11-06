
import random
import os

def GerarDadosAutomaticos():

    tamanho = int(input("\nInsira o Número de dados > "))
    min_ = int(input("Insira o Menor valor onde os dados se encontram > "))
    max_ = int(input("Insira o Maior valor onde os dados se encontram > "))

    ListaDados = []

    for i in range(tamanho):
        ListaDados.append(random.randint(min_,max_))

    return ListaDados

def InserirManualmente():

    ListaDados = []

    tamanho = int(input("\nInsira os dados > "))

    for elements in range(tamanho):

        Dados = int(input(f"Dado [{elements + 1}] > "))
        ListaDados.append(Dados)
    
    return ListaDados
     

def InserirArquivo():

    NomeArquivo = input("Insira o Nome do arquivo > ")
    Arquivo = open(f"{NomeArquivo}").split()

def MostrarValores(valores):
    print(f"""
=========================
    |Todos os Valores|
=========================\n
{valores}
""")

def QuantidadeVetores(valores):

    qtdVetores = 0
    
    for elements in range(len(valores)):
        qtdVetores += 1

    print(f"\nA quantidade de vetores presentes é {qtdVetores} unidades")

def MaiorMenorVetor(valores):

    MenorVetor = valores[0]
    MaiorVetor = 0

    contador = 0

    posicaoMenorVetor = 0
    posicaoMaiorVetor = 0

    for elements in valores:
        if elements > MaiorVetor:
            MaiorVetor = elements
            posicaoMaiorVetor = contador + 1 
        if elements < MenorVetor:
            MenorVetor = elements
            posicaoMenorVetor = contador + 1
        
        contador += 1

    print(f"""
====================================
| >> Maior Valor: {MaiorVetor} na {posicaoMaiorVetor}° Posição |
| >> Menor Valor: {MenorVetor} na {posicaoMenorVetor}° Posição |
====================================
""")
    
def SomatorioValores(valores):

    somatorio = 0

    for elements in valores:
        somatorio += elements
    
    print(f"\nO somatorio dos valores é {somatorio}")   

def MediaValores(valores):

    somatorio = 0
    qtdValores = 0

    for elements in valores:
        somatorio += elements
        qtdValores += 1
    
    media = somatorio / qtdValores

    print(f"|A média dos Valores >> {media}|")

    
def QtdValoresPositivos(valores):

    ListaPositivos = []

    contadorPositivos = 0

    for elements in valores:
        if elements >= 0:
            ListaPositivos.append(elements)
            contadorPositivos += 1

    print(f"""
======================
{ListaPositivos}

|Quantidade >> {contadorPositivos}|
======================
""")

def QtdValoresNegativos(valores):
        
    ListaNegativos = []

    contadorNegativos = 0

    for elements in valores:
        if elements < 0:
            ListaNegativos.append(elements)
            contadorNegativos += 1

    print(f"""
======================
{ListaNegativos}

|Quantidade >> {contadorNegativos}|
======================
""")

def Regras(valores):
    opcoes = """
======================================
    >>> Atualizando Valores <<<
======================================
| 1 | - Multiplicar Por Um Valor
| 2 | - Elevar a Um Valor
| 3 | - Reduzir a uma fração
| 4 | - Substituir valores negativos por números aleatórios em faixa(min, max)
| 5 | - Ordenar valores
| 6 | - Embaralhar valores
======================================
"""

    print(opcoes)
    opcoesMenu = int(input("> "))

    
    match opcoesMenu:
        case 1:
            valores = MultiplicarValores(valores)
        case 2: 
            valores = ElevarValor(valores)
        case 3:
            valores = ReduzirAhFracao(valores)
        case 4:
            valores = SubstituirValoresNegativos(valores)
        case 5:
            valores = OrdenarValores(valores)
        case 6:
            valores = EmbaralharValores(valores)
    
    return valores

def clear_screen():

    if os.name == 'posix':  # Linux/macOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')

def MultiplicarValores(valores):

    valor = int(input('\nInforme um valor para os termos serem multiplicados > '))

    for elements in range(len(valores)):
        valores[elements] = valores[elements] * valor

    return valores

def ElevarValor(valores):

    valor = int(input('Informe um valor para os termos serem Elevados > '))

    for elements in range(len(valores)):
        valores[elements] = valores[elements] ** valor

    return valores 

def ReduzirAhFracao(valores):
    
    numerador = int(input("Informe o Valor do Numerador > "))
    Denominador = int(input("\nInforme o Valor do Denominador > "))

    resultadoDivisao = numerador/Denominador

    ListaNova = []

    for elements in valores:
        ListaNova.append(elements * resultadoDivisao)
    
    valores = ListaNova

    return ListaNova

def AddNovosValores(valores):
    
    opcoes = """
======================================
    >>> Adicionando Valores <<<
======================================
| 1 | - Inicializar Dados Automaticos
| 2 | - Inserir Valores Manualmente
| 3 | - Inserir Arquivo
============================
"""
    print(opcoes)

    entrada = int(input("\n> "))

    match entrada:
        case 1:
            valores += GerarDadosAutomaticos()
        case 2:
            valores += InserirManualmente()
        case 3:
            valores += InserirArquivo()

def RemoverPorValor(valores):

    valor = int(input("Informe o valor a ser excluido > "))

    ListaNova = []

    for elements in valores:
        if elements == valor:
            continue
        
        ListaNova.append(elements)

    valores = ListaNova

    (f"|\nValor ({valor}) foi removido ")

    return valores
    
def RemoverPorIndex(valores):

    valor = int(input("Informe o index a ser excluido > "))

    ListaNova = []

    for elements in range(len(valores)):
        if elements + 1 == valor:
            continue
            
        ListaNova.append(valores[elements])

    valores = ListaNova

    print(f"|\nIndex ({valor}) foi removido ")

    return valores

def EditarPorPosicao(valores):

    indexEditado = int(input("Informe o index a ser editado > "))
    valorInserido = int(input("Informe o valor a ser Inserido > "))

    valores[indexEditado - 1] = valorInserido

    print(f"O index {indexEditado}° foi inserido o valor {valorInserido}!")

    print(f"\nA nova Lista de vetores Consiste em {valores}")

def  SalvarArquivo(valores):

    nome_arquivo = input("\nInforme o nome do arquivo > ")

    with open(nome_arquivo, 'w') as arquivo:
        for valor in valores:
            arquivo.write(f"{valor}\n")

    print("\n|Arquivo Salvo|\n")

    return nome_arquivo

def SubstituirValoresNegativos(valores):

    ListaNova = []

    ValorMin = int(input("\nInforme o valor minimo da faixa de substituição > "))
    ValorMax = int(input("Informe o valor maximo da faixa de substituição > "))

    if ValorMin < 0 or ValorMax < 0:
        print("\nNúmeros Abaixo de Zero!! Tente Novamente!!")
        SubstituirValoresNegativos(valores)

    for elements in valores:
        if elements < 0:
            ListaNova.append(random.randint(ValorMin, ValorMax))  
        else: 
            ListaNova.append(elements)

    valores = ListaNova

    print("\n|Valores Negativos Substituidos|")

    return valores

def Resetar(valores):

    ListaNova = []
    
    print("\n|Lista de valores resetada|")

    return ListaNova

def EmbaralharValores(valores):

    IndexAleatorio = random.randint(0,len(valores))
    ListaNova = []
    for elements in range(len(valores)):
        valores[elements], valores[IndexAleatorio] = valores[IndexAleatorio], valores[elements]

    print("\n|Valores Foram Embaralhados|")
        
    return valores

def OrdenarValores(arr):


    # BUBBLE SORT
    
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1):
                if arr[j] > arr[j+1] : 
                        arr[j], arr[j+1] = arr[j+1], arr[j]


    print("\n|Valores Foram Ordenos de Forma Aleatoria|")

    return arr