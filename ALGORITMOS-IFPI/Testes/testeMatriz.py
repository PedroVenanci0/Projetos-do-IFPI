def main():
    matriz = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

    coluna = 3  # Índice da coluna que queremos imprimir

    for linha in matriz:
        # Verifica se a linha tem pelo menos 4 elementos
        if len(linha) > coluna:
            print(linha[coluna])  # Imprime o elemento na coluna 3

main()
