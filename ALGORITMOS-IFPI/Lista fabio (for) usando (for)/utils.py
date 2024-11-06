import sys
import os
import time

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
    tempo = 2
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
    
