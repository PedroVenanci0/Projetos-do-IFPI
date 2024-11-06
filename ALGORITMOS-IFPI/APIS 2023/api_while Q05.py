# [serasa.js] A SERASA começou a implantar o Serasa Score 2.0 em 2021. O Score é uma forma de avaliar o perfil do consumidor no momento da
# aquisição de crédito, seja cartão de crédito ou financiamento de um veículo, apartamento ou empréstimo pessoal. Desta forma são avaliadas algumas
# entradas de dados históricos consumidor e, caso não esteja negativado, apresentando um valor entre 0 e 1000.

# Baseado nisso, faça um programa que receba valores de 0 a 100 em cada um dos 3 critérios de cálculo, ou seja, como se fosse uma Escala, no item a. 
# você pode ter de 0 a 100, se for 100, por exemplo, significa 100% dos pontos previstos, assim Score 1.0 (260) e Score 2.0 (620), se fosse 50%
# então esse item a. seria 130 e 310, respectivamente em cada Score 1.0 e 2.0. Aplique essa formula de cada uma e apresente o valor do Score tanto
# versão Score 1.0 quanto na versão Score 2.0.

# TABELA

from utils import clear_screen

def main():

    print('\n====== SERESA Score. =======\n')

    criteiro_A_total_Serasa_01 = 260
    criteiro_B_total_Serasa_01 = 570
    criteiro_C_total_Serasa_01 = 170

    criteiro_A_total_Serasa_02 = 620
    criteiro_B_total_Serasa_02 = 190
    criteiro_C_total_Serasa_02 = 190

    criteiro_a = int(input('Informe a porcentagem do primeiro criterio(0 a 100)\n >>> '))
    criteiro_b = int(input('Informe a porcentagem do segundo criterio(0 a 100)\n >>> '))
    criteiro_c = int(input('Informe a porcentagem do terceiro criterio(0 a 100)\n >>> '))


    valor_criterio_A_serasa_01 = criteiro_A_total_Serasa_01 * (criteiro_a / 100)
    valor_criterio_B_serasa_01 = criteiro_B_total_Serasa_01 * (criteiro_b / 100)
    valor_criterio_C_serasa_01 = criteiro_C_total_Serasa_01 * (criteiro_c / 100)

    valor_criterio_A_serasa_02 = criteiro_A_total_Serasa_02 * (criteiro_a / 100)
    valor_criterio_B_serasa_02 = criteiro_B_total_Serasa_02 * (criteiro_b / 100)
    valor_criterio_C_serasa_02 = criteiro_C_total_Serasa_02 * (criteiro_c / 100)


    somatorio_serasa_01 = valor_criterio_A_serasa_01 + valor_criterio_B_serasa_01 + valor_criterio_C_serasa_01
    somatorio_serasa_02 = valor_criterio_A_serasa_02 + valor_criterio_B_serasa_02 + valor_criterio_C_serasa_02

    if somatorio_serasa_01 > 800 and somatorio_serasa_01 <= 1000:
        categoria_01 = "\033[32mMUITO BOM\033[m"

    elif somatorio_serasa_01 > 600 and somatorio_serasa_01 <= 800:
        categoria_01 = "\033[34mBOM\033[m"

    elif somatorio_serasa_01 > 400 and somatorio_serasa_01 <= 600:
        categoria_01 = "\033[33mREGULAR\033[m"

    elif somatorio_serasa_01 > 0 and somatorio_serasa_01 <= 400:
        categoria_01 = "\033[31mBAIXO\033[m"

    if somatorio_serasa_02 > 701 and somatorio_serasa_02 <= 1000:
        categoria_02 = "\033[32mMUITO BOM\033[m"

    elif somatorio_serasa_02 > 501 and somatorio_serasa_02 <= 700:
        categoria_02 = "\033[34mBOM\033[m"

    elif somatorio_serasa_02 > 301 and somatorio_serasa_02 <= 500:
        categoria_02 = "\033[33mREGULAR\033[m"

    elif somatorio_serasa_02 > 0 and somatorio_serasa_02 <= 300:
        categoria_02 = "\033[31mBAIXO\033[m"
    
    clear_screen()

    print(f'''
\n=========================================
        >>> SERASA SCORE <<<
=========================================                    
>> SERASA SCORE 1.0 -----> {categoria_01}
>> SERASA SCORE 2.0 -----> {categoria_02}
=========================================
\n''')

    








main()