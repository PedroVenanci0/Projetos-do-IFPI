def main():

    numero_linhas = int(input())

    Lista_strings = []

    for elements in range(numero_linhas):

        text = input()
        Lista_strings.append(text)
        menor_string = text

        Lista_strings.sort()

        string_em_verificacao = True

        for i, string in range(len(Lista_strings)):







        #if len(string) < len(menor_string):
            #menor_string = string

    

    #Lista_strings.sort() Ordena minha lista do menor para o maior
    #nova lista = sorted(Lista_strings) Cria uma nova lista do menor para o maior

    
        
    


# Preciso pegar a menor string e verificar se as demais strings cumpriram suas regras de criação.

# Regras: Não pode adciocinar nenhum caractere ao meio da string, 
# nao pode remover caracteres apos adiciondos

# Com base na menor string foram feitas as demais, ent apos pegar a menor string da minha lista
# preciso ver se a "segunda menor string" está criada corretamente
# verificando nela as regras acima, e assim po diante.
        
main()