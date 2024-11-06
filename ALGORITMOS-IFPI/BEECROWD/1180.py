def main():

    N = int(input())
    valores = list(map(int,input().split()))

    menorValor = valores[0]

    for i in range(len(valores)):
        if valores[i] < menorValor:
            menorValor = valores[i]
            posicaoValor = i
    
    print(f"Menor valor: {menorValor}")
    print(f"Posicao: {posicaoValor}")


main()