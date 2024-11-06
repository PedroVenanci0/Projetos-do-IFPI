
import utils

def main():

    opcao = int(input(menu()))
    
    match opcao:

        case 1:
            utils.clear_screen()
            mais20()
        case 2:
            utils.clear_screen()
            has_no_e()
        case 3:
            utils.clear_screen()
            avoids()
        case 4:
            utils.clear_screen()
            uses_only()
        case 5:
            utils.clear_screen()
            uses_all()
        case 6:
            utils.clear_screen()
            is_abecedarian()

def has_no_e():

    arquivo = open('words.txt')

    Lista_no_eh = []

    for linha in arquivo:
        palavra = linha.strip()

        contem_eh = False
        
        for elements in palavra:
            if elements == "e":
                contem_eh = True
                break

        if not contem_eh: 
            Lista_no_eh.append(palavra)

    for elements in Lista_no_eh:
        print(elements)

def mais20():

    fin = open("words.txt")
    for line in fin:
        word = line.strip()

        if len(word) >= 20:
            print(word)

def avoids():

    arquivo = open("words.txt")

    letras_proibidas = input("Informe as letras proibidas > ")

    Lista_no = []
    proibidas = []
    cont = 0

    
    for elements in letras_proibidas:
        proibidas.append(elements)
        

    for linha in arquivo:
        palavra = linha.strip()
        contem_letra = False

        for elements in palavra:
            for letra in proibidas:
                if elements == letra:
                    contem_letra = True
                    break
            
        if not contem_letra:
            Lista_no.append(palavra)


    for elements in Lista_no:
        print(elements)
        cont += 1


    print(f"\n > N° de palavras que não possuem Letras Proibidas <\n\n>>> {cont} palavras<<<")

def uses_only():

    arquivo = open("words.txt")
    letras_selecionadas = input("Informe as letras: ")

    Lista_letras = []

    for elements in letras_selecionadas:
        Lista_letras.append(elements)

    for linha in arquivo:
        palavra = linha.strip()
        contem = True
        
        for letra in palavra:
            palavra_selecionada = False

            for permitidas in Lista_letras:
                if letra == permitidas:
                    palavra_selecionada = True
                    break

            if not palavra_selecionada:
                contem = False
                break

        if contem:
            print(palavra)

def uses_all():

    arquivo = open("words.txt")

    Letras_obrigatorias = input("Informe as letras obrigatórias: ")

    
    for linha in arquivo:
        palavra = linha.strip()
        todas_as_letras_presentes = True

        
        for letra in Letras_obrigatorias:
            letra_encontrada = False
            for caracter in palavra:
                if caracter == letra:
                    letra_encontrada = True
                    break
            
            if not letra_encontrada:
                todas_as_letras_presentes = False
                break
        
        
        if todas_as_letras_presentes:
            print(palavra)

def is_abecedarian():

    palavras_ordenadas = []
    arquivo = open('words.txt')  
    
    for linha in arquivo:
        palavra = linha.strip()
        
        ordem = True
        for i in range(len(palavra) - 1):
            if palavra[i] > palavra[i + 1]:
                ordem = False
                break
        
        if ordem:
            palavras_ordenadas.append(palavra)
    
    for elemensts in palavras_ordenadas:
        print(elemensts)

def menu():
    opção = """
===============================================
  Qual filtro você deseja aplicar no arquivo?
===============================================

  1 - Palavras com mais de 20 letras
  2 - Palavras que não possuem a letra 'e'
  3 - Palavras que nao contem letras Proibidas
  4 - Palavras Somente da Lista de Palavras Selecionadas
  5 - Palavras onde deve ter todas as letras da Lista Selecionada pelo menos uma vez
  6 - Palavras que suas letras se encontram em ordem Alfabetica

===============================================
>>> """
    return opção

main()
