# [piscina.js] Uma piscina é algo muito legal de ter (um amigo que
# tem uma). Para evitar transbordar ao tomar banho na piscina é
# bom deixar o nível da água com no máximo 85% da capacidade.
# Assim uma piscina que comporta 20 mil litros de água é bom botar
# só 17mil litros. Considere uma piscina estilo quadrada. Para
# encher a piscina ele usará água paga (o valor é cobrado por cada
# 1000 litros de água, em partes inteiras. Ou seja, se usar 1 litro já
# paga por 1000, ao usar 1002 já paga 2 mil litros)

# a. Calcule a capacidade máxima da piscina pedindo ao usuário as
# dimensões de largura, comprimento e profundidade (em cm). 1 litro é
# igual a 1000 cm3
# . Uma piscina por exemplo de capacidade →
# L=100cm x C=100cm x P=100cm → 1000 litros, e deve ser cheia até
# 850 litros apenas.

# b. Informe até quantos litros é recomendado encher a piscina.

# c. Peça ao usuário para informar o valor a ser pago por cada 1000 litros
# na concessionária de água de sua cidade, e informe quanto ele
# gastará para encher sua piscina;

# d. Mensalmente é necessário repor 10% da água devido a banho e
# evaporação, informe ao usuário também o gasto mensal para manter
# a piscina no nível ideal.

def main():

    print('\n=================================')
    print ('  >>>>> MEDIDAS DA PISCINA <<<<<')
    print('=================================\n')   

    largura = float(input('>>> Informe o valor da largura (em cm): '))
    comprimento = float(input('>>> Informe o valor da comprimento (em cm): '))
    profundidade = float(input('>>> Informe o valor da profundidade (em cm): '))

    capacidade_max_piscina = (largura * comprimento * profundidade) / 1000
    capacidade_recomendada = capacidade_max_piscina * (85/100)

    print (f"""
           
===================================
>>>> Custo de reposição ao mês <<<<<
===================================

>>>> Capacidade Maxima:          \033[36m{capacidade_max_piscina:.2f}\033[m
>>>> Capacidade recomendada:     \033[36m{capacidade_recomendada:.2f}\033[m
""")
    
    print('\n======================================')
    print ('>>>> Custo para ter uma piscina <<<<<')
    print('======================================\n') 

    valor_pago = float(input('>>>> Informe o valor a ser pago por cada 1000 L de água: '))

    pagamento_total = calculando_pagamento_total(capacidade_recomendada, valor_pago)
    
    print (f"""
>>>> Valor gasto para encher a piscina até sua capacidade resomendada:  \033[32m{pagamento_total:.3f}\033[m R$
""")
    
    print('\n===================================')
    print ('>>>> Custo de reposição ao mês <<<<<')
    print('===================================\n')

    valor_mes = calculando_valor_mes(capacidade_recomendada, valor_pago)
    
    print (f"""
>>> O valor pago ao mês para a reposição de 10% de água é \033[32m{valor_mes} reais\033[m R$
\n""")


def calculando_valor_mes(capacidade_recomendada, valor_pago):
    reposição_do_mes = capacidade_recomendada * (10/100)
    
    if  reposição_do_mes > 1000:
       quantidade_de_vezes = (reposição_do_mes // 1000) + 1
       valor_mes = quantidade_de_vezes * valor_pago
    
    else:
        valor_mes = valor_pago

    return valor_mes
    
def calculando_pagamento_total(capacidade_recomendada, valor_pago):

    quantidade_de_vezes_que_ira_pagar = capacidade_recomendada // 1000
    pagamento_total = quantidade_de_vezes_que_ira_pagar * valor_pago

    if capacidade_recomendada % 1000 != 0:
        pagamento_total = pagamento_total + valor_pago

    return pagamento_total
    
main()
