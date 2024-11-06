from utils import escrever_texto
from utils import clear_screen
import time
import random

def UtilizandoWhile():

    print("""
> Opeções de Tarefas:
_________________________________
          
> (1) < Calcular o Fatorial de um número N.
> (2) < Imprimir uma Sequência Fibonacci de comprimento C.
> (3) < Função que imprime uma Sequência Simples de A até B.
> (4) < Calcular o Produto (multiplicação) nas forma de somas sucessivas.
> (5) < Calcular Exponencial de um Número N elevado a expoente E.
> (6) < Dado um intervalo A e B, calcular o somatório de um Vetor de N Elementos Aleatórios.
> (7) < Contar Vogais e Consoantes de Frase.
_________________________________
""")
    
    opcoes = int(input("> "))

    match opcoes:
        case 1:
            FatorialWhile()
        case 2:
            FibonacciWhile()
        case 3:
            SequenciaWhile()
        case 4:
            ProdutoSomaSucessivasWhile()
        case 5:
            ExponencialWhile()
        case 6:
            SomatorioAleatorioWhile()
        case 7:
            ContarVogaisConsoantesWhile()


def FatorialWhile():

    texto = "\nInforme um valor: "
    escrever_texto(texto)
    N = int(input("> "))

    start_time = time.time()

    iteravel = 1
    contador = N

    while contador > 1:
        iteravel *= contador
        contador -= 1

    end_time = time.time()
    execution_time = end_time - start_time

    clear_screen()

    print(f"""
        >>> Fatorial While <<<
========================================
O fatorial {N}!   >   {iteravel}
Tempo de execução >   {execution_time:.6f} segundos
========================================
""")
    

def FibonacciWhile():

    texto = "\nInforme um valor: "
    escrever_texto(texto)
    N = int(input("> "))
        
    primeiro_termo = 0
    segundo_termo = 1
    
    fibonacci = [primeiro_termo, segundo_termo]

    start_time = time.time()
    
    while N > 2:
        proximo_termo = primeiro_termo + segundo_termo
        fibonacci.append(proximo_termo)
    
        primeiro_termo = segundo_termo
        segundo_termo = proximo_termo

        N -= 1
    
    sequencia_fibonacci = ", ".join(map(str, fibonacci))

    end_time = time.time()
    execution_time = end_time - start_time

    clear_screen()
    
    print(f"""
      >>> Sequência fibonacci <<<
========================================
Termos da Sequência  >   {sequencia_fibonacci}
Tempo de execução    >   {execution_time:.6f} segundos
========================================
""")
    
def SequenciaWhile():

    texto = "\nInforme o range da Sequência de Valores (A B): "
    escrever_texto(texto)
    A,B= map(int, (input("> ").split()))

    start_time = time.time()

    ListaValores = []

    while A <= B:
        ListaValores.append(A)
        A += 1

    end_time = time.time()
    execution_time = end_time - start_time

    clear_screen()

    print(f"""
      >>> Sequência Simples <<<
========================================
Termos da Sequência  >   {ListaValores}
Tempo de execução    >   {execution_time:.6f} segundos
========================================
""")


def ProdutoSomaSucessivasWhile():

    texto = "\nInforme os Valores (A B): "
    escrever_texto(texto)
    A,B= map(int, (input("> ").split()))

    start_time = time.time()

    contador = 0
    soma = 0 

    while contador < B:
        soma += A 
        contador += 1
    
    end_time = time.time()
    execution_time = end_time - start_time

    clear_screen()

    print(f"""
>>> Produto de Somas Sucessivas <<<
========================================
Valor do Produto Final  >   {soma}
Tempo de execução    >   {execution_time:.6f} segundos
========================================
""")

def ExponencialWhile():

    clear_screen()
    
    texto = "\nInforme os Valores (A B): "
    escrever_texto(texto)
    A,B= map(int, (input("> ").split()))

    start_time = time.time()

    contador = 0
    soma = 1

    while contador < B:
        soma *= A
        contador += 1
    
    end_time = time.time()
    execution_time = end_time - start_time


    print(f"""
>>> Produto de Somas Sucessivas <<<
========================================
Valor do Produto Final  >   {soma}
Tempo de execução    >   {execution_time:.6f} segundos
========================================
""")


def SomatorioAleatorioWhile():

    texto = "\nInforme o range da Sequência de Valores (A B): "
    escrever_texto(texto)
    A,B= map(int, (input("> ").split()))

    texto = "\nInforme o Numero de elementos: "
    escrever_texto(texto)
    N = int(input("> "))

    start_time = time.time()
    ListaValores = []

    contadorElementos = 0

    while contadorElementos < N:
        ListaValores.append(random.randint(A,B))
        contadorElementos += 1
    
    contador = 0
    somatorio = 0
    
    while contador < len(ListaValores):
        somatorio += ListaValores[contador]
        contador += 1

    end_time = time.time()
    execution_time = end_time - start_time

    clear_screen()

    print(f"""
      >>> Sequência Simples <<<
========================================
Termos da Sequência  >   {ListaValores}
Somatorio de Termos  >   {somatorio}
Tempo de execução    >   {execution_time:.6f} segundos
========================================
""")


def ContarVogaisConsoantesWhile():

    texto = "\nInforme um Texto: "
    escrever_texto(texto)
    T = (input("> ")).upper()

    start_time = time.time()

    vogais = "AEIOU"
    consoantes = "BCDFGHJKLMNPQRSTVWXYZ"

    contador = 0
    N_consoante = 0
    N_vogais = 0

    while contador < len(T):
        caractere = T[contador]

        if caractere in vogais:
            N_vogais += 1
        elif caractere in consoantes:
            N_consoante += 1
        contador += 1
    
    end_time = time.time()
    execution_time = end_time - start_time

    clear_screen()

    print(f"""
      >>> Sequência Simples <<<
========================================
Texto Atual          > {T}
Número de consoantes > {N_consoante}
Número de vogais     > {N_vogais}
Tempo de execução    > {execution_time:.6f} segundos
========================================
""")       
