import sys, os, time, functools

# Adiciona o caminho da pasta utils ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

def limites_min_max(mensagem, min, max):
    numero = (int(input(mensagem)))
    if numero < min or numero > max:
        print ('Número inválido! Digite novamente')
        return limites_min_max(mensagem, min, max)
    return numero

# Função para limpar a tela
def clear_screen():
    # Verifica o sistema operacional
    if os.name == 'posix':  # Linux/macOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')
    
def aguarde():
    tempo_inicial = time.time()
    tempo = 4
    while time.time() - tempo_inicial < tempo:  
        for i in range(tempo + 1):  
            print("Aguarde" + "." * i, end="\r")  
            time.sleep(0.5)  
        print("Aguarde   ", end="\r")  
        time.sleep(0.5)  

def tabela_de_cor(): 

    cor = 'cor'
    print (f'''
   >>>> NÚMEROS PARA CORES DOS RESULTADOS <<<<
           
           CINZA        >>>        \033[30m{cor} = 30\033[m
           VERMELHOR    >>>        \033[31m{cor} = 31\033[m
           VERDE        >>>        \033[32m{cor} = 32\033[m
           AMARELO      >>>        \033[33m{cor} = 33\033[m
           AZUL ESCURO  >>>        \033[34m{cor} = 34\033[m
           ROSA         >>>        \033[35m{cor} = 35\033[m
           AZUL CIANO   >>>        \033[36m{cor} = 36\033[m
''')


def OutputColor(NameColor,argument):

    DicionaryColor = {
        "gray": "30m",
        "red": "31m",
        "green": "32m",
        "yellow": "33m",
        "blue": "34m",
        "pink": "35m",
        "cyan": "36m"
    }

    return (f"\033[{DicionaryColor[f'{NameColor}']}{argument}\033[m")

def cor_cinza(argumento):
    print (f'\033[30m{argumento}\033[m')

def cor_vermelho(argumento):
    print (f'\033[31m{argumento}\033[m')

def cor_verde(argumento):
    print (f'\033[32m{argumento}\033[m')

def cor_amarelo(argumento):
    print (f'\033[33m{argumento}\033[m')

def cor_azuk_escuro(argumento):
    print (f'\033[34m{argumento}\033[m')

def cor_rosa(argumento):
    return f'\033[35m{argumento}\033[m'

def cor_ciano(argumento):
    return f'\033[36m{argumento}\033[m'


def myStrip(delimitador, valores):
    stringFormatada = ""

    valores = str(valores)

    for elements in valores:
        if elements == delimitador:
            continue
        else: 
            stringFormatada += elements
        
    print(stringFormatada)

def mysplit(delimitador, valores):

    ListaValores = []
    string = ""

    for elements in valores:
        if str(elements) == delimitador:
            ListaValores.append(string)
            string = ""
            continue
        else:
            string += str(elements)

    if string != "":
        ListaValores.append(string)

    print(ListaValores)


def myfilter(function, valores):
        
        ListaNova = []

        for elements in  valores:
            if function(elements):
                ListaNova.append(elements)

        return ListaNova

def myMap(function, valores):
    
    ListaNova = []

    for elements in  valores:
        ListaNova.append(function(elements))
        
    return ListaNova

def myReduce(function, valores):

    ValorFinal = 0

    for elements in  valores:
        ValorFinal = function(ValorFinal,elements)
    
    return ValorFinal

def main():
    
    lista = [ 1, 2, 58, 345]

    ListaPrinciapl = myMap(lambda x: x + x, lista)

    print(ListaPrinciapl)

def escrever_texto(texto):
    delay = 0.09
    for elements in texto:
        print(elements, end='', flush=True)  # Exibe o caractere sem quebra de linha e força a exibição imediata
        time.sleep(delay)  # Atraso antes de exibir o próximo caractere
    print()

main()