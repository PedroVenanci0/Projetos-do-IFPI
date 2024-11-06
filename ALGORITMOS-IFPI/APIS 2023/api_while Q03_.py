# [investimento.js] Mariana resolveu investir de parte de seu salário
# (um pedaço(R$) inferior a 30%) de forma fixa mensal; O investimento
# escolhido rende mensalmente a uma taxa de juros de 0,01% até 1,00
# % sobre o saldo do mês. Mariana tem um dado objetivo com este
# investimento. Pergunte a ela qual o objetivo e de quanto ela precisa
# para realizá-lo. Além disso, peça o salário, quanto(%) ela pretende
# investir mensalmente e qual a taxa de juros do investimento
# escolhido. Em seguida mostre em quantos meses ela atingirá o
# objetivo. Se for acima de 12 meses mostre-o em anos e meses. A
# cada mês você deve atualizar o saldo primeiro com o aporte
# (depósito de valor do salário) e depois aplicar os créditos dos juros
# sobre esse novo saldo. Faça isso enquanto o objetivo não for
# alcançado, contando os meses para serem exibidos como se pede.

import os
import time

def main(): 

    porcentagem_investimento = 30+1
    taxa_juros = 1+1
        
    # ENTRADA

    while porcentagem_investimento >= 30 and taxa_juros > 1:

        print ('\n-----> Quanto tempo até a conclusão do seu objetivo? Vamos descobrir... <------\n')

        objetivo = input('>>> Diga-me qual seu objetivo: ')
        preço_objetivo = float(input('>>> Qual o valor do objetivo: '))
        salario = float(input('>>> Informe sua renda mensal: '))
        porcentagem_investimento = float(input('\n>>>Quantos porcento do salario vc deseja investir (investimento inferior a 30% do salario): '))

        if porcentagem_investimento >= 30:
            print ('investimento demasiadamente alto!!')
            porcentagem_investimento = float(input('Qunatos porcento do salario vc deseja investir (investimento inferior a 30% do salario): '))

        taxa_juros = float(input('\n>>> Qual a taxa de juros escolhida (taxa menor ou igual a "1"): '))

        if taxa_juros > 1:

            print ('Taxa demasiadamente alta!!')
            taxa_juros = float(input('Qual a taxa de juros escolhida(taxa menor ou igual a "1"): '))


    tempo_ate_objetivo = 0
    valor_investido_com_juros = 0
    anos = 0
    

    print('\n>>> CAPITAL ACUMULADO POR MÊS <<<\n')

    # PROCESSAMENTO

    tempo_ate_objetivo = 0
    valor_investido_com_juros = 0
    anos = 0

    valor_investido = (salario * (porcentagem_investimento/100))

    while valor_investido_com_juros < preço_objetivo:

        valor_investido_com_juros += valor_investido 

        valor_investido_com_juros *= (taxa_juros + 100) / 100

      # valor_investido_com_juros += (valor_investido * (taxa_juros/100)) + valor_investido
        tempo_ate_objetivo += 1

        print(f'>>> SALDO NO {tempo_ate_objetivo}° MÊS: {valor_investido_com_juros:.2f}\n')

    if tempo_ate_objetivo >= 12:

        anos = tempo_ate_objetivo // 12
        meses = tempo_ate_objetivo % 12

    else:

        meses = tempo_ate_objetivo

    enter = input('Pressione ENTER para ver o resultado: ')
    clear_screen()
    print("Processando...")
    aguarde()
    clear_screen()
    
    # SAIDA

    print (f"""
----------------------------------------
>>>> TEMPO ATE O SONHO <<<<<
----------------------------------------\n
=================================================================================================
>>>> O TEMPO ATE A COMPRA DO OBJETIVO ({objetivo}) CORRESPONDE A {anos} ANOS E {meses} MESES <<<<
=================================================================================================
PS: VC CONSEGUE!!!!!
""")
    
# Função para limpar a tela
def clear_screen():
    # Verifica o sistema operacional
    if os.name == 'posix':  # Linux/macOS
        os.system('clear')
    elif os.name == 'nt':   # Windows
        os.system('cls')
    
def aguarde():
    tempo_inicial = time.time()
    tempo = 4

    while time.time() - tempo_inicial < tempo:  
        for i in range(tempo + 1):  
            print("Aguarde" + "." * i, end="\r")  
            time.sleep(0.5)  
        print("Aguarde   ", end="\r")  
        time.sleep(0.5)  

def calculando_saldo(preço_objetivo, salario, porcentagem_investimento, taxa_juros):

    tempo_ate_objetivo = 0
    valor_investido_com_juros = 0
    anos = 0

    while valor_investido_com_juros < preço_objetivo:

        valor_investido = (salario * (porcentagem_investimento/100))

        valor_investido_com_juros += valor_investido * (taxa_juros/100) + valor_investido

        tempo_ate_objetivo += 1

        print(f'>>> SALDO NO {tempo_ate_objetivo}° MÊS: {valor_investido_com_juros:.2f}\n')
    
     
main()