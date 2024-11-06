# 29. Escreva um algoritmo que calcula o retorno de um investimento financeiro. O usuário deve informar
# quanto será investido por mês e qual será a taxa de juros mensal. O algoritmo deve informar o saldo do
# investimento após um ano (soma das aplicações mensais + juros compostos), e perguntar ao usuário se
# deseja calcular o ano seguinte, sucessivamente. Por exemplo, caso o usuário deseje investir R$ 100,00
# por mês, e tenha uma taxa de juros de 1% ao mês, o algoritmo forneceria a seguinte saída:
# Saldo do investimento após 1 ano: 1268.25
# Deseja processar mais um ano (S/N) ?


def main():

    print ('>>>> CALCULO DE INVESTIMENTOS <<<< ')

    deseja_calcular = input('Deseja processar um ano de investimento(S/N) ? ')
    montante = 0

    while (deseja_calcular != "N"):

        valor_investido = float(input('Informe o valor a ser investido ao mês: '))
        taxa_juros = float(input('Informe a taxa de juros mensal: '))

        contagem_mes = 0

        while (contagem_mes <= 12):

            montante += valor_investido * (1 * taxa_juros)**12

            contagem_mes += 1
        
        print (f'Saldo do investimento após 1 ano: {montante}')
        deseja_calcular = input('Deseja processar mais um ano (S/N) ? ')

    print ('fim...')

   






main()