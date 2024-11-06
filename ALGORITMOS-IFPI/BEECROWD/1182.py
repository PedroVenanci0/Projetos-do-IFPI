def main():
    C = int(input())
    T = input().upper()

    matriz = showMatriz()

    match T:
        case "S":
            soma = somatorio(C,matriz)
            print(round(soma,1))
        case "M":
            media = mediaMatriz(C,matriz)
            print(round(media,1))

def somatorio(Coluna,matriz):
    soma = 0

    for linha in matriz:
        soma += linha[Coluna]

    return soma

    
def mediaMatriz(Coluna,matriz):
    soma = somatorio(Coluna,matriz)

    media = soma / len(matriz[Coluna])
    return media

def showMatriz():
    matriz = []

    for i in range(12):
        linha = []
        for vatores in range(12):
            valor = float(input())
            linha.append(valor)
        matriz.append(linha)
        
    return matriz

main()