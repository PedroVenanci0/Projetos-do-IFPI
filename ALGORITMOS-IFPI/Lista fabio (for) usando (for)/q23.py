# 23. Uma determinada empresa armazena para cada funcionário uma ficha contendo o código, o número de
# horas trabalhadas e o seu no de dependentes. Considerando que a empresa paga R$ 12,00 por hora e R$
# 40,00 por dependentes e que sobre o salário são feitos descontos de 8,5% para o INSS e 5% para IR.
# Escreva um algoritmo que leia o código, número de horas trabalhadas e número de dependentes de N
# funcionários. Após a leitura de cada ficha, escreva os valores descontados para cada imposto e o salário
# líquido do funcionário.

def main():
    
    print("""
=======================================
        >>> FICHA SALARIAL <<<
=======================================
""")
    
    numero_funcionario = int(input('>> Informe o número de funcionarios: '))
    
    for i in range(numero_funcionario):
        
        print (f'\n====== INSERINDO INFORMAÇÕES DO {i + 1}° FUNCIONARIO =======\n')
        
        codigo = int(input('>> Informe o código de identificação: '))
        hrs_trabalhadas = int(input('\n>> Informe o número de horas trabalhadas: '))
        numero_de_dependentes = int(input('\n>> Informe o número de dependentes do funcionario: '))
        
        salario_bruto = (hrs_trabalhadas * 12 + numero_de_dependentes * 40)
        inss = (salario_bruto * 8.5/100)
        ir = (salario_bruto * 5/100)
        salario_liquido = salario_bruto * 86.5/100
        
        print(f"""
    
==============================================================
        >>>>>>>>>> {i + 1}° FUNCIONARIO <<<<<<<<<<<<<
==============================================================
            
- O Salario BRUTO                     ----> \033[34m{salario_bruto:.2f}\033[m
- Valor descontado pelo INSS (8.5%)   ----> \033[31m{inss:.2f}\033[m
- Valor descontado pelo IR (5%)       ----> \033[31m{ir:.2f}\033[m
- O Salario Liquido                   ----> \033[32m{salario_liquido:.2f}\033[m
            
==============================================================
""")
        
main()