# 1. [gift.js] Uma loja presenteia suas clientes com descontos
# (cashback) progressivos de acordo com suas compras. Desta
# forma, para compras mensais de até R$ 250 reais, é feita a
# conversão (geração) de cashback de 5%; Para compras acima de
# R$ 250 até R$ 500, 7% de cashback; De R$ 500 até R$ 750, 8%
# de cashback; E para compras acima de R$ 750 é aplicado
# primeiramente as regras anteriores até R$ 750 do valor em cada
# faixa, e 25% sobre o valor acima de R$ 750. Operações de
# cashbacks progressivos têm o objetivo de incentivar as suas
# clientes a comprarem mais e ao mesmo tempo serem
# compensadas por isso.
# a. Implemente um software para auxiliar no cálculo do
# cashback mensal de suas clientes (devem ser lidos N
# compras Nome Cliente e Valor Compras).
# b. Informe quanto foi o faturamento total (soma das vendas);
# Quanto foi distribuído em cashback; Qual o valor em reais e
# percentual investido em cashback pela loja; Maior, menor e
# valor médio pago em cashback.

from utils import clear_screen

def main():
    print ('>>>>> gift cards <<<<<')
    # flag (0) para numero_de_comrpras,nome_cliente e valor_compras
    
    somatorio_vendas_totais = 0
    somatorio_cashback = 0
    contador_cashback = 0 
    numero_clientes = 1

    print(f'''

=====================================
            \033[33m{numero_clientes}° Cliente\033[m 
=====================================
''')

    nome_cliente = input('\033[33m>>>\033[m Informe o nome do cliente: ')
    numero_de_compras = int(input('\033[33m>>>\033[m Informe o numero de compras: '))
    valor_compras = int(input('\033[33m>>>\033[m Informe o valor da compra: '))

    valor_pago_pelo_cliente = calculando_valor_pago_pelo_cliente(numero_de_compras, valor_compras)
    cashback = calculando_caskback(numero_de_compras, valor_compras)
    
    maior_cashback = cashback
    menor_cashback = cashback

    while numero_de_compras != 0:
        valor_pago_pelo_cliente = calculando_valor_pago_pelo_cliente(numero_de_compras, valor_compras)
        cashback = calculando_caskback(numero_de_compras, valor_compras)
        
        if cashback > maior_cashback:
            maior_cashback = cashback
        
        if cashback < menor_cashback:
            menor_cashback = cashback
        
        contador_cashback += 1
        somatorio_vendas_totais += valor_pago_pelo_cliente
        somatorio_cashback += cashback

        numero_clientes += 1

        print(f'''

=====================================
            \033[33m{numero_clientes}° Cliente\033[m 
=====================================
''')

        nome_cliente = input('\033[33m>>>\033[m Informe o nome do cliente: ')
        numero_de_compras = int(input('\033[33m>>>\033[m Informe o numero de compras: '))
        valor_compras = int(input('\033[33m>>>\033[m Informe o valor da compra: '))

    porcentagem_cashback = ((somatorio_cashback * 100) / somatorio_vendas_totais)
    valor_medio = somatorio_cashback / contador_cashback

    clear_screen()
    print (f"""

                \033[33m>>>> VENDAS CASHBACK <<<<\033[m
================================================================       
\033[33m.\033[m O FATURAMENTO TOTAL FOI DE \033[32m{somatorio_vendas_totais:.2F}\033[m R$
\033[33m.\033[m O VALOR TOTAL DISTRIBUIDO DE CASHBACK FOI DE \033[31m{somatorio_cashback:.2F}\033[m R$
\033[33m.\033[m O MAIOR VALOR DE CASHBACK FOI DE \033[34m{maior_cashback:.2F}\033[m R$
\033[33m.\033[m O MENOR VALOR FOI DE \033[34m{menor_cashback:.2f}\033[m R$
\033[33m.\033[m O VALOR MEDIO DE CASKBACK FOI DE \033[34m{valor_medio:.2F}\033[m R$
\033[33m.\033[m O VALOR PERCENTUAL INVESTIDO EM CASHBACK FOI DE \033[31m{porcentagem_cashback:.2F}\033[m %
================================================================
""")
    
def calculando_valor_pago_pelo_cliente(numero_compras, valor_compras):
       
    somatorio_vendas_individual = valor_compras * numero_compras

    if somatorio_vendas_individual <= 250:
        valor_pago_pelo_cliente = (somatorio_vendas_individual * (95/100))

        return valor_pago_pelo_cliente

    elif somatorio_vendas_individual > 250 and somatorio_vendas_individual <= 500:
        valor_pago_pelo_cliente = (somatorio_vendas_individual * (93/100))

        return valor_pago_pelo_cliente

    elif somatorio_vendas_individual > 500 and somatorio_vendas_individual <= 750:
        valor_pago_pelo_cliente = (somatorio_vendas_individual * (92/100))

        return valor_pago_pelo_cliente
        
    elif somatorio_vendas_individual > 750:
        sobra = (somatorio_vendas_individual - 750)
        sobra_com_desconto = (sobra * 75/100)
        valor_pago_pelo_cliente = (750 * (92/100)) + sobra_com_desconto

        return valor_pago_pelo_cliente
    
def calculando_caskback(numero_compras, valor_compras):
     
    somatorio_vendas_individual = valor_compras * numero_compras

    if somatorio_vendas_individual <= 250:
        cashback = (somatorio_vendas_individual * 5/100)

        return cashback
        
    elif somatorio_vendas_individual > 250 and somatorio_vendas_individual <= 500:
        cashback = (somatorio_vendas_individual * 5/100)

        return cashback

    elif somatorio_vendas_individual > 500 and somatorio_vendas_individual <= 750:
        cashback = (somatorio_vendas_individual * 5/100)

        return cashback
        
    elif somatorio_vendas_individual > 750:
        sobra = (somatorio_vendas_individual - 750)
        cashback_01 = (sobra * 25/100)
        cashback_02 = (750 * (8/100))
        cashback = cashback_01 + cashback_02

        return cashback
main()
