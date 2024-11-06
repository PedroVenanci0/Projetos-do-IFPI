
import funcionalidades
from utils import red,green,darkblue,lightblue,clear_screen,pink,gray,yellow

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
            funcionalidades.StartGame()
        case 2:
            funcionalidades.Tutorial()
        case 3:
            funcionalidades.HistoricoVitoria()
        case 4:
            funcionalidades.PassarVenancio()
        case 0:
            clear_screen()
            print("Fim...")
            return
        case _:
            menu()

        

def main():
    menu()
main()


