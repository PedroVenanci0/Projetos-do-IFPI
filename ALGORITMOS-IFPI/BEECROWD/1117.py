def main():  
    valida_nota01 = 0
    valida_nota02 = 0
    nota_01 = 1
    nota_02 = 1
    while nota_01 != valida_nota01:
        nota_01 = float(input(''))
        if nota_01 <= 10 and nota_01 >= 0:
            valida_nota01 = nota_01
        else:
            print ('nota invalida')
    while nota_02 != valida_nota02:
        nota_02 =  float(input(''))
        if nota_02 <= 10 and nota_02 >= 0:
            valida_nota02 = nota_02
        else:
            print ('nota invalida')
    media = (valida_nota01 + valida_nota02) / 2
    print(f'media = {media:.2f}')
main()