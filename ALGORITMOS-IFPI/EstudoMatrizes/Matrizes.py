def main():
    matrizes = [[2,1,3,4,5,6],[2,2,1,9],[8,3,2,6]]

    for linhas in range(len(matrizes)):
        for colunas in range(len(matrizes[linhas])):
            matrizes[linhas][colunas] = int(input(f"Informe o valor dos valores [{linhas}][{colunas}]: "))
    
    print("-=-" * 20)

    for linhas in range(len(matrizes)):
        for colunas in range(len(matrizes[linhas])):
            print(f"[{matrizes[linhas][colunas]:^5}]",end="")
            
        print()
    print("-=-" * 20)

    #variavel_teste = [int(x) for x in range(0, 10): if]
            
main() 