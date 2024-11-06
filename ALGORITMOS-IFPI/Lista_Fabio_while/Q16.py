# 16. Uma companhia financeira debita um juro de 0.85% diário sobre o saldo não pago de um empréstimo.
# Com um empréstimo de R$ 3.000,00, um pagamento de R$ 200,00 é feito todo dia útil. Escreva um
# algoritmo que calcule quantos dias úteis são necessários para se concluir o pagamento do empréstimo.


def main():

    emprestimo = 3000
    periodo = 0

    while (emprestimo > 0):

        juros_diarios = emprestimo * 0.0085  
        pagamento_diario = 200
        emprestimo = (emprestimo + juros_diarios) - pagamento_diario
        periodo += 1
    
    print (periodo)


main()