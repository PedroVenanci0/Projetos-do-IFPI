def main():
    
    arquivo = open('arquivo.txt', 'r')

    linhas = arquivo.readlines()

    linhas = map(str.strip, linhas)

    for linha in linhas:
        print(linha)

    arquivo.close()


main()
