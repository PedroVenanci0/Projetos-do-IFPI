def forma_02():
    numero_N = int(input('\n>>> Digite até qual número você deseja descobrir seus pares.\n>>> '))
    for i in range(1, numero_N + 1):
        if i % 2 == 0:
            print(i)

def forma_01():
    numero_N = int(input('\n>>> Digite até qual número você deseja descobrir seus pares.\n>>> '))
    lista_numeros = [i for i in range(numero_N + 1)]
    filtro_par = list(filter(lambda i: i % 2 == 0, lista_numeros))
    print(filtro_par)  

def main():
    print('\n================================')
    print('>>> SELEÇÃO DE NÚMEROS PARES <<<')
    print('================================\n')

    selecione_forma = int(input('>>> Selecione uma das formas disponiveis para a seleção dos pares, (1) e (2): '))

    if selecione_forma == 1:
        forma_01()
    elif selecione_forma == 2:
        forma_02()
    else:
        while selecione_forma != 1 and selecione_forma != 2:
            selecione_forma = int(input('>>> Selecione uma das formas disponiveis para a seleção dos pares, (1) e (2): '))

main()
