
def main():

    while True:

        numero_linhas = int(input())

        if numero_linhas == 0:
            break

        Lista_strings = []
        maior_string = ""

        for elements in range(numero_linhas):
            
            text = input()

            Lista_strings.append(text)
            
            if len(text) > len(maior_string):
                maior_string = text

        text_complet = ""

        for strings in Lista_strings:

            string_formatada = ""
            elements_anteior = " "

            for elements in strings:

                if elements_anteior != elements:
                    string_formatada += elements
                elements_anteior = elements

                #if len(string_formatada) > len(maior_string):
                    #maior_string = text
    
            while len(string_formatada) < len(maior_string):
                string_formatada = " " + string_formatada
            text_complet += "\n" + string_formatada

        print(text_complet)

main()
