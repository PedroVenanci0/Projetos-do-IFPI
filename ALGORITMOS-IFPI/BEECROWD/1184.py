def main():

    O = input().upper()

    matriz = ShowMatriz()

    match O:
        case "S":
            soma = SomatorioMatriz(matriz)
            print(round(soma,1))
        case "M":
            media = MediaMatriz(matriz)
            print(round(media,1))

def ShowMatriz():
    matriz = []

    for i in range(12):
        linha = []
        for elements in range(12):
            linha.append(float(input()))
        matriz.append(linha)
        
    return matriz

def SomatorioMatriz(matriz):

    soma = 0
    NumeroValores = 0
    for i in range(len(matriz)):
        linha = matriz[i]
        soma_linha = 0
        for j in range(len(linha), i-1):
            NumeroValores += 1
            soma_linha += linha[j]
        soma += soma_linha
    

    return soma

def MediaMatriz(matriz):

    soma = 0
    NumeroValores = 0
    for i in range(len(matriz)):
        linha = matriz[i]
        soma_linha = 0
        for j in range(len(linha), i-1):
            NumeroValores += 1
            soma_linha += linha[j]
        soma += soma_linha

    media = soma / NumeroValores

    return media

main()