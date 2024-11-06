def main():
    L = int(input())
    T = input().upper()

    matriz = showMatriz()

    match T:
        case "S":
            soma = somatorio(L,matriz)
            print(soma)
        case "M":
            media = mediaMatriz(L,matriz)
            print(media)

def somatorio(Linha,matriz):
    soma = 0

    for valor in matriz[Linha] :
        soma += valor
    return soma

    
def mediaMatriz(L,matriz):
    soma = somatorio(L,matriz)

    media = soma / len(matriz[L])
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