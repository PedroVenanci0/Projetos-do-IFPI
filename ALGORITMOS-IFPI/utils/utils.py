import sys, os, time, functools

# Adiciona o caminho da pasta utils ao sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'utils'))

def limites_min_max(mensagem, min, max):
    numero = (int(input(mensagem)))
    if numero < min or numero > max:
        print ('Número inválido! Digite novamente')
        return limites_min_max(mensagem, min, max)
    return numero

def clear_screen():
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


def gray(argumento):
    return (f'\033[30m{argumento}\033[m')

def red(argumento):
    return (f'\033[31m{argumento}\033[m')

def green(argumento):
    return (f'\033[32m{argumento}\033[m')

def yellow(argumento):
    return (f'\033[33m{argumento}\033[m')

def darkblue(argumento):
    return (f'\033[34m{argumento}\033[m')

def pink(argumento):
    return f'\033[35m{argumento}\033[m'

def lightblue(argumento):
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

def escrever_texto(texto):
    delay = 0.09
    for elements in texto:
        print(elements, end='', flush=True)  # Exibe o caractere sem quebra de linha e força a exibição imediata
        time.sleep(delay)  # Atraso antes de exibir o próximo caractere
    print()

