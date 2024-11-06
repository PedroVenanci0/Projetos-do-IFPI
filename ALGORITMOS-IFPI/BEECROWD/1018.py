def main():
    
    valor_inteiro = int(input())
    valor_inteiro_conservado = valor_inteiro
    
    contador_nota_100 = valor_inteiro // 100
    valor_inteiro %= 100
    
    contador_nota_50 = valor_inteiro // 50
    valor_inteiro %= 50
    
    contador_nota_20 = valor_inteiro // 20
    valor_inteiro %= 20
    
    contador_nota_10 = valor_inteiro // 10
    valor_inteiro %= 10
    
    contador_nota_5 = valor_inteiro // 5
    valor_inteiro %= 5
    
    contador_nota_2 = valor_inteiro // 2
    valor_inteiro %= 2
    
    contador_nota_1 = valor_inteiro
    
    print(f"{valor_inteiro_conservado}")
    print(f"{contador_nota_100} nota(s) de R$ 100,00")
    print(f"{contador_nota_50} nota(s) de R$ 50,00")
    print(f"{contador_nota_20} nota(s) de R$ 20,00")
    print(f"{contador_nota_10} nota(s) de R$ 10,00")
    print(f"{contador_nota_5} nota(s) de R$ 5,00")
    print(f"{contador_nota_2} nota(s) de R$ 2,00")
    print(f"{contador_nota_1} nota(s) de R$ 1,00")

main()
