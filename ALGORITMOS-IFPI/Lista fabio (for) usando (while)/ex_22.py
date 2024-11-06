# 22. Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
# nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
# numero de identificação e o peso do boi mais magro e do boi mais gordo.


def main():

    # entrada

    numero_de_fichas = int(input("Número de fichas: "))

    contador = 1

    peso_boi_magro = 1000
    peso_boi_gordo = 0

    nome_mais_gordo = ""
    nome_mais_magro = ""

    identificacao_magro = 0

    while contador <= numero_de_fichas:

        print(f">> FICHA N° {contador} <<")

        nome_boi = input("\nInforrme o nome do bolvino: ")
        identificacao = int(input("Informe o numero de identificação do bolvino: "))
        peso_boi = float(input("Informe o peso do boi: "))


        if peso_boi > peso_boi_gordo:

            nome_mais_gordo = nome_boi
            peso_boi_gordo = peso_boi
            identificacao_gordo = identificacao
        
        if peso_boi < peso_boi_magro:

            nome_mais_magro = nome_boi
            peso_boi_magro = peso_boi
            identificacao_magro = identificacao

        contador += 1
    
    # saida

    print(f'''
          
                >>>> É boi <<<<<
===================================================\n
-------->        Boi mais PESADO          <-------\n
- NOME                    >>> {nome_mais_gordo}
- Número de identificação >>> \033[32m{identificacao_gordo}\033[m N°
- PESO                    >>> \033[31m{peso_boi_gordo}\033[m (kg)
          
-------->        Boi mais LEVE            <-------\n
- NOME                    >>> {nome_mais_magro}
- Número de identificação >>> \033[32m{identificacao_magro}\033[m N°
- PESO                    >>> \033[31m{peso_boi_magro}\033[m (kg)
          
''')

main()