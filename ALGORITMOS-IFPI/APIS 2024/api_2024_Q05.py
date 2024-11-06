
# 05. Ajude Leandro a fazer uma Pesquisa de Valores no
# supermercado. Apresente para ele um sistema de Menu com
# opções para Incluir Item (Descrição, Especificação e Valor). Vá
# acumulando isso numa lista em String, um item por linha e, no
# final, um valor total. Deve ser possível incluir Item e Imprimir Lista,
# apenas. Além claro da opção sair.

# ——- PESQUISA DE PREÇOS —---
# 1 - Arroz (5 kg) R$ 27,50
# 2 - Feijão (1 kg) R$ 7,99
# 3 - Leite Líquído (1L) R$ 4,69
# —----------------------------------------
# Valor total: R$ 40,18

# Deixe os valores R$ em alinhados verticalmente, como acima,
# inclusive a vírgula. Mostra ainda as opções parcelamento do
# cartão bem como o valor das parcelas, conforme regras abaixo.:

# Até R$ 30 não é possível parcela.

# A partir de R$ 30 até R$ 100 é possível parcelar em até 3x

# Acima de R$ 100 é possível parcelar em até 5x

# Qualquer valor é possível parcelar em até 6x, porém nesse caso
# Tem-se Juros Compostos (ou seja, que se acumulam em cada
# parcela para calcular a próxima) com taxa de 5% a.m.
# Ou seja, para toda compra é possível pagar à vista, ou ainda ter
# um ou duas formas de parcelamento,

from utils import clear_screen

def main():

    print("""
===================================================
            >>> MERCADO VENÂNCIO <<<
===================================================
""")
    
    menu = """
-------------- MENU -----------------
1 - Incluir item
2 - Mostrar lista de itens inclusos

0 - Sair 
--------------------------------------
>>> """

    opcao_menu = 1
    contador_produtos = 0
    lista_produtos = ''
    valor_total = 0

    while opcao_menu != 0:

        opcao_menu = int(input(menu))
        clear_screen()

        if opcao_menu == 1:

            contador_produtos += 1

            descricao = input('>> Informe a descrição do produto: ')
            especificacao = input('\n>> Informe a especificação do produto (kg/L): ')
            valor = float(input('\n>> Informe o valor do produto:  '))

            lista_produtos += f'\n{contador_produtos}° - {descricao} ({especificacao}) R$ {valor})' 

            valor_total += valor
 

        elif opcao_menu == 2:

            produtos_e_parcelas = calculando_produtos_e_parcelamento(valor_total, lista_produtos, valor)

            print(produtos_e_parcelas)
            
            deseja_sair = input('\n>> Deseja voltar para o menu (PRESSIONE ENTER): ')
            clear_screen()

def calculando_produtos_e_parcelamento(valor_total, lista_produtos, valor):

        parcela_composta_sem_juros = valor_total / 6

        for i in range(6):

            juros_composto = parcela_composta_sem_juros * (5 / 100)
            parcela_composta_sem_juros += juros_composto

            parcela_composta = parcela_composta_sem_juros

        if valor_total < 30:

            return (f"""             
======= PESQUISA DE PREÇOS =======
{lista_produtos}
—---------------------------------
Valor total: R$ {valor_total:.2f} 
----------------------------------
PARCELAMENTO: VALOR TOTAL DA COMPRA MUITO BAIXO PARA SER PARCELADO
PARCELAMENTO COMPOSTO EM ATÉ 6x DE {parcela_composta:.2f}
----------------------------------
""")
        elif valor_total >= 30 and valor_total <= 100:

            parcela_30_100 = valor_total / 3

            return (f"""             
======= PESQUISA DE PREÇOS =======
{lista_produtos}
—---------------------------------
>> Valor total: R$ {valor_total} 
----------------------------------
>> PARCELAMENTO SIMPLES EM ATÉ 3 VEZES DE {parcela_30_100:.2f}
>> PARCELAMENTO COMPOSTO EM ATÉ 6x DE {parcela_composta:.2f}
----------------------------------
""")

        elif valor_total > 100:
            parcela_100 = valor_total / 5

            return (f"""             
======= PESQUISA DE PREÇOS =======
{lista_produtos}
—---------------------------------
Valor total: R$ {valor_total} 
----------------------------------
PARCELAMENTO SIMPLES EM ATÉ 5x DE {parcela_100:.2f} 
PARCELAMENTO COMPOSTO EM ATÉ 6x DE {parcela_composta:.2f}
----------------------------------
""")

main()