# 30. Escreva um algoritmo que leia o nome de um produto, o preço e a quantidade comprada. Escreva o
# nome do produto comprado e o valor total a ser pago, considerando que são oferecidos descontos pelo
# número de unidades compradas, segundo a tabela abaixo: (FLAG: nome do produto = “FIM”).
# a. Até 10 unidades: valor total
# b. de 11 a 20 unidades: 10% de desconto
# c. de 21 a 50 unidades: 20% de desconto
# d. acima de 50 unidades: 25% de desconto

def main():

    print (' ##### SUPERMERCADO VENÂNCIO ###### ')
    
    nome_produto = input('Informe o nome do produto: ')

    while nome_produto != "FIM":

        preço_produto = float(input('Informe o preço do produto: '))
        qtd_comprada = float(input('Quantidade do produto: '))
    
        valor_total = preço_produto * qtd_comprada

        if qtd_comprada <= 10:

            print(f"""
                  
                      . PRODUTO >>> {nome_produto}
                      . QUANTIDADE SOLICITADA >>> {qtd_comprada}
                      . VALOR TOTAL A SER PAGO >>> {valor_total}

        """)
        
        elif qtd_comprada > 10 and qtd_comprada <= 20:

            valor_total = valor_total - (valor_total * 10/100) 

            print(f"""
                  
                      . PRODUTO >>> {nome_produto}
                      . QUANTIDADE SOLICITADA >>> {qtd_comprada}
                      . VALOR TOTAL A SER PAGO >>> {valor_total}

        """)
        
        
        elif qtd_comprada > 20 and qtd_comprada <= 50:

            valor_total = valor_total - (valor_total * 20/100) 

            print(f"""
                  
                      . PRODUTO >>> {nome_produto}
                      . QUANTIDADE SOLICITADA >>> {qtd_comprada}
                      . VALOR TOTAL A SER PAGO >>> {valor_total}

        """)
        
        elif qtd_comprada > 50:

            valor_total = valor_total - (valor_total * 25/100)

            print(f"""
                  
                      . PRODUTO >>> {nome_produto}
                      . QUANTIDADE SOLICITADA >>> {qtd_comprada}
                      . VALOR TOTAL A SER PAGO >>> {valor_total}

        """)

        
        nome_produto = input('Informe o nome do produto: ')
    
    print ('FIM DO CALCULO DAS COMPRAS!!! ESPERO QUUE TENHA GOSTADO E VOLTE SEMPRE!!!')




main()