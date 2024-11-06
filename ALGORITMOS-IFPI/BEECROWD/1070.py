def main():
    
    valor_X = int(input())
    
    contador_impar = 0 
    
    while (contador_impar != 6):

        if valor_X % 2 == 1:

            print (valor_X)
        
            contador_impar += 1
        
        valor_X += 1

main()