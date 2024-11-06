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
    tempo = 4
    while time.time() - tempo_inicial < tempo:  
        for i in range(tempo + 1):  
            print("Aguarde" + "." * i, end="\r")  
            time.sleep(0.5)  
        print("Aguarde   ", end="\r")  
        time.sleep(0.5)  