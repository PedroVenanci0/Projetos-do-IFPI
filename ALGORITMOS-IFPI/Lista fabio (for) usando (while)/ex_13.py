# 13. Leia N e uma lista de N números e escreva o maior número da lista.

def main():

    print(">> Descobrindo o maior número da lista << \n")

    tamanho_lista = int(input("Informe o tamanho da lista: "))

    verificando_tamanho = 0
    ordem_lista = ""

    maior_elemento = 0

    while tamanho_lista != verificando_tamanho:

        add_numero = float(input("Adicione um número a lista: "))
        ordem_lista += str(verificando_tamanho + 1) + "° - " + str(add_numero) + "\n"
        verificando_tamanho += 1
        
        if add_numero > maior_elemento:
            maior_elemento = add_numero

    print(f"""
>>> Lista de Números <<< 
------------------------

{ordem_lista}
------------------------
. Total de elementos: {tamanho_lista}
. Maior elemento: {int(maior_elemento)}
""")

main()