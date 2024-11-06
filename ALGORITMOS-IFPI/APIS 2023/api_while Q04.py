# 4. [empréstimo.js] João precisa de um dinheiro emprestado para
# comprar um Notebook para estudar programação. Para isso, foi ao
# RSBank fazer uma simulação. As taxas de empréstimo do banco
# obedecem à regra dos Juros Compostos Mensais, ou seja, o valor é
# calculado cumulativamente mês a mês, ou seja, aplica-se os juros
# sobre o valor total no primeiro mês e esse passa a ser a base para o
# segundo mês.

# Porém a taxa de juros aplicada é calculada de acordo com o prazo
# de parcelamento (vide tabela) e à SELIC, atualmente em 13,75%
# (abril/2023). O usuário só pode parcelar o empréstimo em até 24x
# (min. 2 parcelas). Valor mínimo de empréstimo é de um salário
# mínimo. Valor máximo de parcela é 40% da Renda Mensal do Cliente.
# Antes de calcular os juros é necessário calcular o IOF (Imposto sobre
# Operações Financeiras) pago ao Governo Federal antes de aplicar
# os Juros. O IOF é calculado da seguinte forma: 0,38% sobre valor
# total (independente do prazo) + 0,0082% por cada dia do prazo do
# empréstimo. Considere todos os meses com 30 dias. Os juros são
# aplicados sobre o valor a ser recebido pelo Cliente + IOF
# Prazo Taxa
# Até 6x 50% da SELIC
# de 7x a 12x 75% da SELIC
# de 12x a 18x 100% da SELIC
# Acima de 18x 130% da SELIC

# ● Peça ao usuário Renda Mensal, Valor Empréstimo e Prazo
# desejados, valide os dados a serem recebidos.

# ● Calcule e escreva na tela:
# a. Valor Pedido
# b. Valor do IOF
# c. Valor dos Juros a pagar
# d. Valor Total a pagar (ex.: "R$ 5148,00")
# e. Valor da Parcela Mensal (ex.: "16x de R$ 321,75")
# f. Comprometimento da Renda Mensal (%)
# g. Se Empréstimo APROVADO ou NEGADO (se a
# renda mensal suporta a parcela)

import os
import time

def main():

    print ('\n                #### RSBank ####                    \n')
    print ('           VAMOS CALCULAR SEU EMPRESTIMO?\n')

    validacao = 0
    fim_do_processo = 0
    salario_minimo = 1350
    Selic = 13.75
    valor_emprestimo_IOF = 0
    valor_total = 0

    while validacao != 1:

        renda_mensal = float(input('Informe sua renda mensal: '))
        valor_emprestimo = float(input('Informe o valor do emprestimo: '))
        prazo = int(input('Informe o numero de parcelas(mês): '))

        if valor_emprestimo >= salario_minimo and prazo <= 24 and prazo >= 2:

            validacao = 1

        else:
        
            print('Informeções Invalidas!! Tente novamente.')
            
            if renda_mensal == 0:

                fim_do_processo = 1
                validacao = "APROVADO"

    # CALCULANDO IOF
            
    prazo_em_dias = prazo * 30 # TRANSFORMANDO O PRAZO DE MESES EM DIAS

    valor_emprestimo_IOF = valor_emprestimo

    for elements in range(prazo_em_dias): # PRIMEIRA PARTE DO VALOR DO IOF (0.0082% POR DIA DO EMPRESTIMO)

        valor_emprestimo_IOF += valor_emprestimo_IOF * (0.0082/100)

    IOF = (valor_emprestimo_IOF * 0.38/100)

    # calculando parcela

    valor_parcela = (valor_emprestimo + IOF) / prazo

    # calculando taxa de juros (SELIC) 

    total_a_pagar = valor_parcela

    if prazo <= 6:
        juros = (50/100) * Selic

    elif prazo >= 7 and prazo < 12:
        juros = (75/100) * Selic

    elif prazo >= 12 and prazo <= 18:
        juros = Selic
        
    elif prazo > 18:
        juros = (130/100) * Selic

    # valor total a ser pago

    for elements in range(prazo):

        valor_total += total_a_pagar + (total_a_pagar * (juros/100))


        # O valor foi aprovado? 

    compromentimento_mensal = ((valor_parcela * 100) / renda_mensal)

    if compromentimento_mensal < 40:

        validadando_emprestimo = "APROVADO"

    else:

        validadando_emprestimo = ("NEGADO")
        
    if fim_do_processo != 1:

        clear_screen()

        print(f'''
                        >>>> CARTA DE EMPRESTIMO <<<<
        ==================================================================
        . VALOR PEDIDO                      ----> {valor_emprestimo:.0f} R$
        . VALOR DO IOF                      ----> {IOF:.2f} R$
        . VALOR DO JUROS                    ----> {juros:.2f}%
        . VALOR TOTAL A PAGAR               ----> {valor_total:.2f} R$
        . VALOR DA PARCELA                  ----> {valor_parcela:.2f} R$
        . COMPROMENTIMENTO DA RENDA MENSAL  ----> {compromentimento_mensal:.2f}%
        ===================================================================
        ''')

        mostrar_resultado = input('PRESSIONE ENTER PARA VISUALIZAR O RESULTADO: ') 

        clear_screen()
        print('Processando dados.')
        aguarde()
        clear_screen()

        print(f'''    
    ============================================
        >>> SEU EMPRESTIMO FOI \033[32m{validadando_emprestimo}\033[m <<<
    ============================================
        ''')

# Função para limpar a tela
def clear_screen():
    # Verifica o sistema operacional
    if os.name == 'posix':  # Linux/macOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')
    
def aguarde():
    tempo_inicial = time.time()
    tempo = 3

    while time.time() - tempo_inicial < tempo:  
        for i in range(tempo + 1):  
            print("Aguarde" + "." * i, end="\r")  
            time.sleep(0.5)  
        print("Aguarde   ", end="\r")  
        time.sleep(0.5) 

main()