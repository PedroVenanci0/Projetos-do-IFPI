def main():

    arquivo = open('arquivo.txt', 'w') 

    for i in range(62):
        
        arquivo.write(f'Linha {i}: Escrita em Python\n')

    arquivo.close()


main()
