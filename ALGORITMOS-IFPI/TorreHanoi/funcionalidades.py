from utils import red,green,darkblue,lightblue,clear_screen,pink,gray,yellow
import random
import time
import os

R = red("R")
G = green("G")
B = darkblue("B")

def StartGame():

    clear_screen()

    print("> Nome dos players <")
    print("====================")

    Player01 = input("\nPlayer 01 > ")
    Player02 = input("Player 02 > ")

    clear_screen()
    
    print(f"""
===================================
 > Escolha o nivel de {pink("Dificuldade")} <
===================================
          
(1) - Nível {green("Iniciante")}     (Somente 1 torre com 9 itens)
(2) - Nível {yellow("Intermediario")} (3 torres com 6 itens)
(3) - Nível {red("Avançado")}      (3 Torres com 8 itens)
          
===================================
""")
    
    OpcaoNivel = int(input("Informe o nivel Escolhido > "))


    match OpcaoNivel:

        case 1:
            StartNivelIniciante(Player01,Player02)
        case 2:
            StartNivelIntermediario(Player01,Player02)
        case 3:
            StartNivelAvancado(Player01,Player02)
        case _:
            clear_screen()
            print(f"{red("\nOpção Invalida, Tente Novamente!!")}")
            input("\nPressione Enter para voltar ao Seleção de Players...")
            StartGame()

            


def StartNivelIniciante(Player01, Player02):

    ContadorJogadasPlayer01 = 0

    MatrizTorres = CriandoMatrizIniciante()

    clear_screen()
             
    print("\n> Player 01 <\n")

    StartTimePlayer01 = time.time()

    MostrarTorres(MatrizTorres)

    while True:

        validação = validandoFinal(MatrizTorres)

        if validação == True:
            EndTimePlayer01 = time.time()
            TotalTimePlayer01 = EndTimePlayer01 - StartTimePlayer01
            break

        else:
            jogada = input(f"\n{ContadorJogadasPlayer01+1}° movimento:  ").upper()
            ContadorJogadasPlayer01 += 1
            movendoItens(jogada, MatrizTorres)
            clear_screen()
            print("\n> Player 01 <\n")
            MostrarTorres(MatrizTorres)


    ContadorJogadasPlayer02 = 0

    MatrizTorres = CriandoMatrizIniciante()

    clear_screen()
             
    print("\n> Player 02 <\n")

    StartTimePlayer02 = time.time()

    MostrarTorres(MatrizTorres)

    while True:

        validação = validandoFinal(MatrizTorres)

        if validação == True:
            EndTimePlayer02 = time.time()
            TotalTimePlayer02 = EndTimePlayer02 - StartTimePlayer02
            break

        else:
            jogada = input(f"\n{ContadorJogadasPlayer02+1}° movimento:  ").upper()
            ContadorJogadasPlayer02 += 1
            movendoItens(jogada, MatrizTorres)
            clear_screen()
            print("\n> Player 02 <\n")
            MostrarTorres(MatrizTorres)

        
    FimDeJogo(TotalTimePlayer01, TotalTimePlayer02, ContadorJogadasPlayer01, ContadorJogadasPlayer02, Player01, Player02)


def StartNivelIntermediario( Player01, Player02):
    
    ContadorJogadasPlayer01 = 0

    MatrizTorres = CriandoMatrizIntermediario()

    clear_screen()

    print("\n> Player 01 <\n")

    StartTimePlayer01 = time.time()

    MostrarTorres(MatrizTorres)

    while True:

        validação = validandoFinal(MatrizTorres)

        if validação == True:
            EndTimePlayer01 = time.time()
            TotalTimePlayer01 = EndTimePlayer01 - StartTimePlayer01
            break

        else:
            jogada = input(f"\n{ContadorJogadasPlayer01+1}° movimento:  ").upper()
            ContadorJogadasPlayer01 += 1
            movendoItens(jogada, MatrizTorres)
            print()
            clear_screen()
            print("\n> Player 01 <\n")
            MostrarTorres(MatrizTorres)

    
    ContadorJogadasPlayer02 = 0

    MatrizTorres = CriandoMatrizIntermediario()

    clear_screen()

    print("\n> Player 02 <\n")

    StartTimePlayer02= time.time()

    MostrarTorres(MatrizTorres)

    while True:

        validação = validandoFinal(MatrizTorres)

        if validação == True:
            EndTimePlayer02 = time.time()
            TotalTimePlayer02 = EndTimePlayer02 - StartTimePlayer02
            break

        else:
            jogada = input(f"\n{ContadorJogadasPlayer02+1}° movimento:  ").upper()
            ContadorJogadasPlayer02 += 1
            movendoItens(jogada, MatrizTorres)
            print()
            clear_screen()
            print("\n> Player 02 <\n")
            MostrarTorres(MatrizTorres)
    
    FimDeJogo(TotalTimePlayer01, TotalTimePlayer02, ContadorJogadasPlayer01, ContadorJogadasPlayer02,Player01,Player02)

def StartNivelAvancado( Player01, Player02):
    
    ContadorJogadasPlayer01 = 0

    MatrizTorres = CriandoMatrizAvancado()

    clear_screen()

    print("\n> Player 01 <\n")

    StartTimePlayer01 = time.time()

    MostrarTorres(MatrizTorres)

    while True:

        validação = validandoFinal(MatrizTorres)

        if validação == True:
            EndTimePlayer01 = time.time()
            TotalTimePlayer01 = EndTimePlayer01 - StartTimePlayer01
            break

        else:
            jogada = input(f"\n{ContadorJogadasPlayer01+1}° movimento:  ").upper()
            ContadorJogadasPlayer01 += 1
            movendoItens(jogada, MatrizTorres)
            print()
            clear_screen()
            print("\n> Player 01 <\n")
            MostrarTorres(MatrizTorres)

    
    ContadorJogadasPlayer02 = 0

    MatrizTorres = CriandoMatrizAvancado()

    clear_screen()

    print("\n> Player 02 <\n")

    StartTimePlayer02= time.time()

    MostrarTorres(MatrizTorres)

    while True:

        validação = validandoFinal(MatrizTorres)

        if validação == True:
            EndTimePlayer02 = time.time()
            TotalTimePlayer02 = EndTimePlayer02 - StartTimePlayer02
            break

        else:
            jogada = input(f"\n{ContadorJogadasPlayer02+1}° movimento:  ").upper()
            ContadorJogadasPlayer02 += 1
            movendoItens(jogada, MatrizTorres)
            print()
            clear_screen()
            print("\n> Player 02 <\n")
            MostrarTorres(MatrizTorres)
    
    FimDeJogo(TotalTimePlayer01, TotalTimePlayer02, ContadorJogadasPlayer01, ContadorJogadasPlayer02, Player01, Player02)


def MostrarTorres(matriz):
    altura_max = 9  

    print("Estado atual das torres:")
    
    for i in range(altura_max - 1, -1, -1):
        # Exibe os itens das torres, alinhados
        print(f"      {matriz[0][i] if i < len(matriz[0]) else '-'}                     "
              f"{matriz[1][i] if i < len(matriz[1]) else '-'}                  "
              f"{matriz[2][i] if i < len(matriz[2]) else '-'}")
        

    print(F"{red("Torre Vermelha")}          {green("Torre Verde")}       {darkblue("Torre Azul")}")
    print("-" * 30)

def movendoItens(jogada,matriz):

    if jogada == "RB":
        if not VerificacaoTorreVazia(matriz, 0):
            ItemMovido = matriz[0][-1]
            matriz[0].pop()
            matriz[2].append(ItemMovido)

    if jogada == "RG":
        if not VerificacaoTorreVazia(matriz, 0):
            ItemMovido = matriz[0][-1]
            matriz[0].pop()
            matriz[1].append(ItemMovido)
        
    if jogada == "GR":
        if not VerificacaoTorreVazia(matriz, 1):
            ItemMovido = matriz[1][-1]
            matriz[1].pop()
            matriz[0].append(ItemMovido)

    if jogada == "GB":
        if not VerificacaoTorreVazia(matriz, 1):
            ItemMovido = matriz[1][-1]
            matriz[1].pop()
            matriz[2].append(ItemMovido)
    
    if jogada == "BG":
        if not VerificacaoTorreVazia(matriz, 2):
            ItemMovido = matriz[2][-1]
            matriz[2].pop()
            matriz[1].append(ItemMovido)

    if jogada == "BR":
        if not VerificacaoTorreVazia(matriz, 2):
            ItemMovido = matriz[2][-1]
            matriz[2].pop()
            matriz[0].append(ItemMovido)


    return matriz


def VerificacaoTorreVazia(matriz, torreAtual):

    for elements in matriz[torreAtual]:
        if elements in [f"{red("R")}", f"{green("G")}", f"{darkblue("B")}"]:
            return False
    return True
  
def CriandoMatrizIniciante():

    MatrizTorres = [
        [],
        [],
        []
]   
    contador = 0

    for i in range(9):

        NumeroSort = random.randint(0,15)

        if NumeroSort < 5:
            MatrizTorres[0].append(f"{red("R")}")
        elif NumeroSort < 10:
            MatrizTorres[0].append(f"{green("G")}")
        else:
            MatrizTorres[0].append(f"{darkblue("B")}")
    
    return MatrizTorres

def CriandoMatrizIntermediario():

    MatrizTorres = [
        [],
        [],
        []
]

    while len(MatrizTorres[0]) < 6 or len(MatrizTorres[1]) < 6 or len(MatrizTorres[2]) < 6:
        
        NumeroSortTorre = random.randint(0, 2)
        NumeroSortitem = random.randint(0, 15)

        if len(MatrizTorres[NumeroSortTorre]) < 6:  
            if NumeroSortitem < 5:
                MatrizTorres[NumeroSortTorre].append(f"{red("R")}")
            elif NumeroSortitem < 10:
                MatrizTorres[NumeroSortTorre].append(f"{green("G")}")
            else:
                MatrizTorres[NumeroSortTorre].append(f"{darkblue("B")}")

    return MatrizTorres

def CriandoMatrizAvancado():
    
    MatrizTorres = [
        [],
        [],
        []
]

    while len(MatrizTorres[0]) < 8 or len(MatrizTorres[1]) < 8 or len(MatrizTorres[2]) < 8 :

        NumeroSortTorre = random.randint(0, 2)
        NumeroSortitem = random.randint(0, 15)

        if len(MatrizTorres[NumeroSortTorre]) < 8:  
            if NumeroSortitem < 5:
                MatrizTorres[NumeroSortTorre].append(f"{red("R")}")
            elif NumeroSortitem < 10:
                MatrizTorres[NumeroSortTorre].append(f"{green("G")}")
            else:
                MatrizTorres[NumeroSortTorre].append(f"{darkblue("B")}")

    return MatrizTorres
    
def validandoFinal(matriz):

    for i in matriz[0]:
        if i != f"{red("R")}":
            return False

    for i in matriz[1]:
        if i != f"{green("G")}":
            return False

    for i in matriz[2]:
        if i != f"{darkblue("B")}":
            return False

    return True

def FimDeJogo(TotalTimePlayer01, TotalTimePlayer02, ContadorJogadasPlayer01, ContadorJogadasPlayer02,Player01,Player02):


    if ContadorJogadasPlayer01 > ContadorJogadasPlayer02:
        vencedor = Player02
        perdedor = Player01

        ContadorPlayerVencedor = ContadorJogadasPlayer02
        ContadorPlayerPerdedor = ContadorJogadasPlayer01

        TempoPlayerVencedor = TotalTimePlayer02
        TempoPlayerPerdedor = TotalTimePlayer01

    elif ContadorJogadasPlayer01 < ContadorJogadasPlayer02:
        vencedor = Player01
        perdedor = Player02

        ContadorPlayerVencedor = ContadorJogadasPlayer01
        ContadorPlayerPerdedor = ContadorJogadasPlayer02

        TempoPlayerVencedor = TotalTimePlayer01
        TempoPlayerPerdedor = TotalTimePlayer02
    
    else:
        if TotalTimePlayer01 > TotalTimePlayer02:
            vencedor = Player01
            perdedor = Player02

            ContadorPlayerVencedor = ContadorJogadasPlayer01
            ContadorPlayerPerdedor = ContadorJogadasPlayer02

            TempoPlayerVencedor = TotalTimePlayer01
            TempoPlayerPerdedor = TotalTimePlayer02
        else:
            vencedor = Player02
            perdedor = Player01

            ContadorPlayerVencedor = ContadorJogadasPlayer02
            ContadorPlayerPerdedor = ContadorJogadasPlayer01

            TempoPlayerVencedor = TotalTimePlayer02
            TempoPlayerPerdedor = TotalTimePlayer01

    clear_screen()
    print(f"""
=============================================
> PARABENS AO COMPLETAREM A TORRE DE HANOI!!! <
=============================================
          
- O VENCEDOR É O PLAYER {vencedor}

               > PLAYER 01 <
============================================ 
> Tempo - {TotalTimePlayer01:.2f} segundos
> N° de Jogadas - {ContadorJogadasPlayer01} movimentos
============================================

               > PLAYER 02 <
============================================ 
> Tempo - {TotalTimePlayer02:.2f} segundos
> N° de Jogadas - {ContadorJogadasPlayer02} movimentos
============================================
""")


    molde = """\
    ==================================
    Nome do Ganhador: {NomeGanhador}
    Tempo do Ganhador: {TempoGanhador}
    Número de Jogadas: {NúmeroJogadasGanhador}
    ==================================
    Perdedor: {NomePerdedor}
    Tempo do Perdedor: {TempoPerdedor}
    Número de Jogadas: {NúmeroJogadasPerdedor}
    ==================================
    """

    dados = {

        "NomeGanhador": f"{vencedor}",
        "TempoGanhador": f"{TempoPlayerVencedor:.2f}",
        "NúmeroJogadasGanhador": f"{ContadorPlayerVencedor}",

        "NomePerdedor": f"{perdedor}",
        "TempoPerdedor": f"{TempoPlayerPerdedor:.2f}",
        "NúmeroJogadasPerdedor": f"{ContadorPlayerPerdedor}"
    }

    conteudo = molde.format(**dados)

    NomeArquivo = 'HistoricoVitorias.txt'

    with open(NomeArquivo, 'a') as arquivo:
        arquivo.write(conteudo + '\n')

    input("\nPressione Enter para voltar ao menu...")
    menu()

def Tutorial():

    clear_screen()

    print(f"""
====================================
> Bem Vindo a Torre de Hanoi ({red("R")}{green("G")}{darkblue("B")}) <
====================================

================
> Sobre o jogo <
================

- Hanói Rogério Gordinho Bonito --> Hanói RGB
- Você esta prestes a Iniciar um Maravilhoso e complexo jogo de Torres, Boa sorte !!!

=============
> controles <
=============

- {R}{G} (Dá pilha {R} para a torre {G})
- {R}{B} (Dá pilha {R} para a torre {B})
- {G}{R} (Dá pilha {G} para a torre {R})
- {G}{B} (Dá pilha {G} para a torre {B})
- {B}{G} (Dá pilha {B} para a torre {G})
- {B}{R} (Dá pilha {B} para a torre {R})

============
 > Regras <
============

- Vence o Jogador que completar todas as Torres com seus itens correspondentes em menos jogadas

- Somente é possível inserir e remover itens no Topo das Torres.

- Em caso de Empate, a vitoria será daquele que completou em menos tempo

- O jogo Encerrar ao alocar corretamente os itens em suas Torres
________________________________________
""")
    input("\nPressione Enter para Voltar ao Menu...")
    menu()

def HistoricoVitoria():

    clear_screen()

    NomeArquivo = "HistoricoVitorias.txt"

    # Verifica se o arquivo existe
    if os.path.exists(NomeArquivo):

        with open(NomeArquivo, 'r') as arquivo:
            conteudo = arquivo.read()

        print("Histórico de Vitórias:\n")
        print(conteudo)

        input("\nPressione Enter para voltar ao Menu...")
        menu()
    else:
        print(red("Nenhum Historico de Vitorias encontrado!!!"))
        input("\nPressione Enter para voltar ao Menu...")
        menu()

def PassarVenancio():

    clear_screen()
    print(f"""

            > Porquê Passar o Venâncio? <
========================================================
                    > PQ ELE É <
💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓
{red("V")} de Valente
{green("E")} de Elegante
{pink("N")} de Notável
{darkblue("Â")} de Ânimo (significa energia ou disposição positiva)
{pink("N")} de Nobre
{lightblue("C")} de Carismático
{red("I")} de Inspirador
{yellow("O")} de Ousado
💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓💓
=========================================================
""")


    input("Pressione Enter para voltar ao Menu...")
    menu()

def menu():

    clear_screen()

    print(F"""
     > Menu Inicial <
==========================
          
(1) {lightblue("Start Game")}
(2) {green("Tutorial")}
(3) {yellow("Historico de Vitorias")}
(4) {pink("Pq passar o Venâncio? ❤")}
          
(0) {red("Quit Game")}
=========================
""")

    opcoes = int(input("> "))

    match opcoes:
        case 1:
            StartGame()
        case 2:
            Tutorial()
        case 3:
            HistoricoVitoria()
        case 4:
            PassarVenancio()
        case 0:
            clear_screen()
            print("Fim...")
            return