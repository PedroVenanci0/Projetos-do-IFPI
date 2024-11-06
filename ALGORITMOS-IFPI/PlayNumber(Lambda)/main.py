
import Vetor_utils
from utils import OutputColor, clear_screen

from cores import red, reset

def main():

    OpcaoMenuInicial = int(input(Menu() + "> "))

    match OpcaoMenuInicial:

        case 1:
            Valores = Vetor_utils.GerarDadosAutomaticos()
        case 2:
            Valores = Vetor_utils.InserirManualmente()
        case 3:
            Valores = Vetor_utils.InserirArquivo()
            print(f"\n{Valores}")
             
    while OpcaoMenuInicial > 3 or OpcaoMenuInicial < 0:

        clear_screen()
        print(f"\nValor Inserido {red}Invalido!!!{reset}\n")
        OpcaoMenuInicial = int(input(Menu() + "> "))

    MenuGeral()
    OpcoesMenuGeral = int(input("> "))

    while OpcoesMenuGeral != 15:

        match OpcoesMenuGeral:

            case 1:
                Vetor_utils.MostrarValores(Valores)
            case 2:
                Valores = Vetor_utils.Resetar(Valores)
            case 3:
                Vetor_utils.QuantidadeVetores(Valores)
            case 4:
                Vetor_utils.MaiorMenorVetor(Valores)
            case 5:
                Vetor_utils.SomatorioValores(Valores)
            case 6:
                Vetor_utils.MediaValores(Valores)
            case 7:
                Vetor_utils.QtdValoresPositivos(Valores)
            case 8:
                Vetor_utils.QtdValoresNegativos(Valores)
            case 9:
                Valores = Vetor_utils.Regras(Valores)
            case 10:
                Vetor_utils.AddNovosValores(Valores)
            case 11:
                Valores = Vetor_utils.RemoverPorValor(Valores)
            case 12:
                Valores = Vetor_utils.RemoverPorIndex(Valores)
            case 13:
                Vetor_utils.EditarPorPosicao(Valores)
            case 14:
                Vetor_utils.SalvarArquivo(Valores)

        input("\n| Pressione Enter para CONTINUAR: |")
        Vetor_utils.clear_screen()
        MenuGeral()
        OpcoesMenuGeral = int(input("> "))
    
    if OpcoesMenuGeral == 15:
        print("\nEncerrando processamento...")

        opcoes = input("\nDeseja sair sem salvar(Y/N)?")

        while opcoes != "Y" and opcoes != "N":
            opcoes = input("\nDeseja sair sem salvar(Y/N)?")

        if opcoes == "N":
            Vetor_utils.SalvarArquivo(Valores)
        else:
            print("\nFim...")
            return

def MenuGeral():

    Vetor_utils.clear_screen()

    opcoes = """
======================================
        >>> Menu PlayNumber <<<
======================================
| 1 | - Mostrar todos os Vetores
| 2 | - Resetar Valor
| 3 | - Ver quantidades de itens do vetor
| 4 | - Ver menor e maior valores e suas posições
| 5 | - Sómatorio de Valores
| 6 | - Média de Valores
| 7 | - Mostrar Valores Positivos e Quantidades
| 8 | - Mostrar Valores Negativos e suas Quantidades
| 9 | - Atualizar Todos os Valores segundo as regras a seguir
| 10| - Adicionar Novos Valores
| 11| - Remover Itens por um Valor exato
| 12| - Remover por Posição 
| 13| - Editar Valores Especificos por Posição
| 14| - Salvar Valores em Arquivo
| 15| - Sair
=====================================
"""
    print(opcoes) 

def Menu():
    opcao_menu = """
======================================
    >>> Inicialização de Vetores <<<
======================================
| 1 | - Inicializar Dados Automaticos
| 2 | - Inserir Valores 
| 3 | - Inserir Arquivo
======================================
"""
    return opcao_menu

main()

