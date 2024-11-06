from utils import escrever_texto
from utils import clear_screen
import time
import random

def UtilizandoRecursividade():

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
            valor = FatorialRecursividade()
            print(valor)
        case 2:
            valor = FibonacciRecursividade()
            print(valor)
        case 3:
            valor = SequenciaRecursividade()
            print(valor)
        case 4:
            valor = ProdutoRecursividade()
            print(valor)
        case 5:
            valor = ExponencialRecursividade()
            print(valor)
        case 6:
            valor = SomatorioAleatorioRecursividade()
            print(valor)
        case 7:
            ContarVogaisConsoantesRecursividade()

def FatorialRecursividade():
        
    texto = "\nInforme um valor: "
    escrever_texto(texto)
    N = int(input("> "))

    start_time = time.time()

    ValorFinal = FatorialProcessamento(N)

    end_time = time.time()
    execution_time = end_time - start_time

    clear_screen()

    return (f"""
        >>> Fatorial While <<<
========================================
O fatorial {N}!      >   {ValorFinal}
Tempo de execução  >   {execution_time:.6f} segundos
========================================
""")

def FatorialProcessamento (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * FatorialProcessamento(n - 1)

def FibonacciRecursividade():

    texto = "\nInforme um valor: "
    escrever_texto(texto)
    N = int(input("> "))

def FibonacciProcessamento(n):
    pass

def SequenciaProcessamento(a, b):

    if a > b:
        return []
    else:
        return [a] + SequenciaProcessamento(a + 1, b)

def SequenciaRecursividade():

    texto = "\nInforme o range da Sequência de Valores (A B): "
    escrever_texto(texto)
    A, B = map(int, input("> ").split())

    sequencia = SequenciaProcessamento(A, B)
    return (f"A sequência de valores entre {A} e {B} é: {sequencia}")
   
def ProdutoRecursividadeProcessamento(a, b):

    if b == 0:
        return 0
    elif b == 1:
        return a
    else:
        return a + ProdutoRecursividadeProcessamento(a, b - 1)

def ProdutoRecursividade():

    texto = "Informe o primeiro número (a) e o segundo número (b): "
    escrever_texto(texto)
    a, b = map(int, input("> ").split())
        
    resultado = ProdutoRecursividadeProcessamento(a, b)
    return(f"O produto de {a} e {b} é: {resultado}")


def ExponencialRecursividadeProcessamento(a, b):

    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * ExponencialRecursividadeProcessamento(a, b - 1)

def ExponencialRecursividade():

    texto = "Informe a base (a) e o expoente (b): "
    escrever_texto(texto)
    a, b = map(int, input("> ").split())
        
    resultado = ExponencialRecursividadeProcessamento(a, b)
    return(f"{a} elevado a {b} é: {resultado}")
 
def AleatorioProcessamento(n, a, b):

    if n <= 0:
        return 0
    else:
        numero_aleatorio = random.randint(a, b)
        return numero_aleatorio + AleatorioProcessamento(n - 1, a, b)

def SomatorioAleatorioRecursividade():

    texto = "Informe o número de termos a serem somados: "
    escrever_texto(texto)

    n = int(input("> "))
        
    texto = "Informe o número inicial (a) e o número final (b): "
    escrever_texto(texto)
    a, b = map(int, input("> ").split())
        
    resultado = AleatorioProcessamento(n, a, b)
    return (f"A soma de {n} números aleatórios entre {a} e {b} é: {resultado}")
   

def ContarVogaisConsoantesRecursividade():
    pass
