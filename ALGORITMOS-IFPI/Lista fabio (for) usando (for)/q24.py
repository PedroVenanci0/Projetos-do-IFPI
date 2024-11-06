# 24. A prefeitura de uma cidade fez uma pesquisa entre seus habitantes, coletando dados sobre o salário e
# número de filhos. Escreva um algoritmo que leia o salário e o número de filhos de N habitantes e
# escreva:
# a) média de salário da população;
# b) média de número de filhos;
# c) percentual de pessoas com salário de até R$ 1.000,00.

def main():

    print("""
========================================================
            >>> Pesquisa IBGE <<<<
========================================================
""")
    
    numero_de_habitantes = int(input('>> Informe o número de habitantes: '))
    
    contador_habitantes_salario = 0
    contador_filhos = 0
    
    somatorio_filhos = 0
    somatorio_salario = 0
    pessoas_de_menor_renda = 0
    
    for i in range(numero_de_habitantes):

        print(f"""
===========================
  >> HABITANTE N° {i + 1} <<
===========================
""")
        salario = float(input('>> Informe seu salario: '))
        filhos = int(input('\n>> Informe o número de filhos: '))
        
        if salario <= 1000:
            
            pessoas_de_menor_renda += 1
    
        somatorio_filhos += filhos
        somatorio_salario += salario
    
    media_salarios = somatorio_salario / numero_de_habitantes
    media_filhos = somatorio_filhos / numero_de_habitantes
    percentual_renda_baixa = (pessoas_de_menor_renda * 100) / numero_de_habitantes
    
    print(f'''
          
========================================================
            >>> Pesquisa IBGE <<<<
========================================================

- MEDIA DE SALARIO DOS HABITANTES        >>> \033[30m{media_salarios:.0f}\033[m  
- MEDIA DE FILHOS DOS HABITANTES         >>> \033[30m{media_filhos:.0f}\033[m  
- PERCENTUAL DE PESSOAS COM BAIXA RENDA  >>> \033[31m{percentual_renda_baixa:.0f}%\033[m 

========================================================
''')
main()