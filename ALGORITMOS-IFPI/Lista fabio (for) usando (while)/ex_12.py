# 12. Leia N e uma lista de N números e escreva a soma e a média de todos os números da lista.

def main():

    print(">>>> Lista de Números <<<<\n")

    tamanho_lista = int(input("Informe o tamanho da lista: \n"))

    verificando_tamanho = 0
    somatorio_lista = 0
    ordem_lista = ""

    while tamanho_lista != verificando_tamanho:

        add_numero = float(input("Adicione um número a lista: "))
        ordem_lista += str(verificando_tamanho + 1) + "° - " + str(add_numero) + "\n"
        somatorio_lista += add_numero 
        verificando_tamanho += 1
        
    media_termos_lista = somatorio_lista / tamanho_lista

    print(f"""
>>> Lista de Números <<< 
------------------------
{ordem_lista}
------------------------
. Total de elementos: {tamanho_lista}
. Somatorio dos elementos: {somatorio_lista}
. Media dos elementos: {media_termos_lista}
""")

main()