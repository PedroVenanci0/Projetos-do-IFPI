# 17. Em um concurso de beleza, cada candidata tem um cartão contendo nome, altura e peso. Escreva um
# algoritmo que leia um conjunto de cartões e escreva o nome e a altura da candidata mais alta e da mais
# baixa; o nome e o peso da candidata mais magra e da mais gorda. (Flag: nome = 'FIM').

def main():

    nome = input('Informe o nome da candidata: ')

    if nome != 'fim':

        altura = float(input('Informe a altura da candidata: '))
        peso = float(input('Informe o peso da candidata: '))

        maior_altura = altura
        menor_altura = altura
        maior_peso = peso
        menor_peso = peso
        nome_mais_alta = nome
        nome_mais_baixa = nome
        nome_de_maior_peso = nome
        nome_de_menor_peso = nome

    while nome != 'fim':

        if altura > maior_altura:
                
            maior_altura =  altura
            nome_mais_alta = nome
        
        if altura < menor_altura:

            menor_altura = altura
            nome_de_menor_peso = nome

        if peso > maior_peso:
                
            maior_peso = peso
            nome_de_maior_peso = nome 

        if peso < menor_peso:

            menor_peso = peso
            nome_de_menor_peso = nome      
        
        nome = input('Informe o nome da candidata: ')

        if nome != 'fim':

            altura = float(input('Informe a altura da candidata: '))
            peso = float(input('Informe o peso da candidata: '))

    print (f"""

    -----> A candidata de maior altura é {nome_mais_alta} -----> altura coreresponde a {maior_altura} m
    -----> A candidata de menor altura é {nome_mais_baixa} -----> altura coreresponde a {menor_altura} m
    -----> A candidata de maior peso é {nome_de_maior_peso} -----> altura coreresponde a {maior_peso} kg
    -----> A candidata de menor peso é {nome_de_menor_peso} -----> altura coreresponde a {menor_peso} kg

""")
            


main()
