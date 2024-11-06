#22. Um fazendeiro possui fichas de controle sobre sua boiada. Cada ficha contém numero de identificação,
# nome e peso (em kg) do boi. Escreva um algoritmo que leia os dados de N fichas e ao final, escreva o
# numero de identificação e o peso do boi mais magro e do boi mais gordo.

def main():

    print("""
========================
>>> CONTROLE DO GADO <<<
========================
""")
    
    numero_de_fichas = int(input('Digite o número de fichas: '))

    print(f"""
============================
       >> {1}° BOI <<
============================
""")
        
    
    nome = input('Informe o nome do boi: ') 
    idetificacao = int(input('Informe o número de identificação: '))
    peso = int(input('Informe o peso do boi (kg): '))
    
    boi_mais_pesado = peso
    boi_mais_magro = peso
    
    idetificacao_mais_pesado = idetificacao
    idetificacao_mais_magro = idetificacao
    
    Nome_pesado = nome
    Nome_magro = nome
    
    
    
    for i in range(1, numero_de_fichas):

        print(f"""
============================
       >> {i + 1}° BOI << 
============================
""")
        nome = input('Informe o nome do boi: ') 
        idetificacao = int(input('Informe o número de identificação: '))
        peso = int(input('Informe o peso do boi (kg): '))
        
        if peso > boi_mais_pesado:
            
            boi_mais_pesado = peso
            idetificacao_mais_pesado = idetificacao
            Nome_pesado = nome
        
        if peso < boi_mais_magro:
            
            boi_mais_magro = peso
            idetificacao_mais_magro = idetificacao
            Nome_magro = nome
        
    
    print(f'''
          
                >>>> É boi <<<<<
===================================================\n
-------->        Boi mais PESADO          <-------\n
- NOME                    >>> {Nome_pesado}
- Número de identificação >>> \033[32m{idetificacao_mais_pesado}\033[m N°
- PESO                    >>> \033[31m{boi_mais_pesado}\033[m (kg)
          
          
-------->        Boi mais LEVE            <-------\n
- NOME                    >>> {Nome_magro}
- Número de identificação >>> \033[32m{idetificacao_mais_magro}\033[m N°
- PESO                    >>> \033[31m{boi_mais_magro}\033[m (kg)
          
''')
        
        
        
        
        
        
        
        

main()