def main():
    N,M = map(int,input().split())

    matriz = []
    contador = 0

    for elements in range(N):
        linha = []
        for colunas in range(M):
            linha.append(int(input()))
        matriz.append(linha)

    print(matriz)


main()