# 13. Leia o salário de funcionários de uma empresa, calcule e escreva o novo salário (segundo os critérios
# descritos abaixo), a soma dos salários atuais, a soma dos salários reajustados e a diferença entre as 2
# somas. (Flag: salário=0)

# De Até Acréscimo
# R$ 0,00       R$ 2.999,99    25 %
# R$ 3.000,00   R$ 5.999,99    20 %
# R$ 6.000,00   R$ 9.999,99    15 %
# Acima de      R$ 10.000,00   10 %

def main():

    salario = ''
    soma_reajuste = 0 
    soma_salario = 0
    numero_funcionarios = 0

    while (salario != 0):

        salario = float(input('Informe o salario do funcionario: '))

        if (salario != 0):

            reajuste = calculando_reajuste(salario)

            print (f'O novo salário é {reajuste}')

            soma_salario += salario 

            soma_reajuste += reajuste

            numero_funcionarios += 1

    diferença_somas = soma_reajuste - soma_salario
        
    
    # SAIDA
    print (f'                            FORAM ANALISADOS {numero_funcionarios} FUNCIONÁRIOS')

    print ('--------------------------------------------------------------------------------------------------------------------------')

    print (f'----------> A soma dos salários atuais é {soma_salario}                                                  ')
    print (f'----------> A soma dos salários reajustados é {soma_reajuste}                                            ')
    print (f'----------> A diferença entre a soma dos salários reajustados e dos atuais é {diferença_somas:.2f}       ')

    print ('__________________________________________________________________________________________________________________________')





def calculando_reajuste(salario):

    if salario <= 2_999.99:

        return (salario * 25/100) + salario
    
    elif salario >= 3_000 and salario <= 5_999.99:

        return (salario * 20/100) + salario
    
    elif salario >= 6000 and salario <= 9_999.99:

        return (salario * 15/100) + salario
    else:

        return (salario * 10/100) + salario
    
main()