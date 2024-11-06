
from utils import clear_screen
from utils import escrever_texto

import FuncionalidadesFor
import FuncionalidadesWhile
import FuncionalidadesRecursividade

def main():

    clear_screen()

    escrever_texto("\n> NESSA TAREFA IREMOS IMPLEMENTAR PARA AS SITUAÇÕES A SEGUIR, FUNÇÕES E PROGRAMAS NAS VERSÕES DEMONSTRADAS ABAIXO\nE VERIFICAREMOS O TEMPO DE EXECUÇÃO DA TAREFA ESCOLHIDA:  ")
    print("\nPressione Enter para continuar...")
    input()
    print("""
> Opeções de Compilamento:
_________________________________
          
> (1) - Utilizando While
> (2) - Utilizando For
> (3) - Utilizando Funções Recursivas
_________________________________
""")
    
    opcoes = int(input("> "))

    match opcoes:
        case 1:
            FuncionalidadesWhile.UtilizandoWhile()
        case 2:
            FuncionalidadesFor.UtilizandoFor()
        case 3:
            FuncionalidadesRecursividade.UtilizandoRecursividade()

main()