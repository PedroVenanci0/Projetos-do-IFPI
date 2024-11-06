# 27. Escreva um algoritmo que leia um conjunto de dados de um grupo de 100 pessoas, sexo (1=Masculino,
#  2=Feminino), idade e estado civil (1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo) e escreva:
# · Média de idade das mulheres;
# · Média de idade dos homens;
# · O percentual de homens solteiros;
# · O percentual de mulheres solteiras;
# · A quantidade de mulheres divorciadas acima de 30 anos.

def main():

    contador_pessoas = 0
    contador_mulheres = 0
    contador_homens = 0
    contador_homens_solteiros = 0
    contador_mulheres_solteiros = 0 
    somatorio_idades_mulheres = 0
    somatorio_idades_homens = 0
    quantidade_de_mulheres_divorciadas = 0
    
    while (contador_pessoas < 5):

        sexo = int(input('Informe seu sexo(1=Masculino, 2=Feminino):  '))
        idade = int(input('Informe sua idade: '))
        estado_civil = int(input('Informe seu estado civil (1=Casado, 2=Solteiro, 3=Divorciado, 4=Viúvo): '))

        if sexo == 2:

            somatorio_idades_mulheres += idade
            contador_mulheres += 1

            if estado_civil == 2:

                contador_mulheres_solteiros += 1
            
            if estado_civil == 3 and idade > 30:

                quantidade_de_mulheres_divorciadas += 1
        
        if sexo == 1:

            somatorio_idades_homens += idade
            contador_homens += 1

            if estado_civil == 2:

                contador_homens_solteiros += 1
        
        contador_pessoas += 1

    media_idade_homens = (somatorio_idades_homens / contador_homens)
    media_idade_mulheres = (somatorio_idades_mulheres / contador_mulheres)
    porcentagem_homens_solteiros = (contador_homens_solteiros * 100) / contador_homens
    porcentagem_mulheres_solteiras = (contador_mulheres_solteiros * 100) / contador_mulheres

    print (f"""

    · Média de idade das mulheres >>> {media_idade_mulheres:.0f} ANOS
    · Média de idade dos homens >>> {media_idade_homens:.0f} ANOS
    · O percentual de homens solteiros >>> {porcentagem_homens_solteiros}%
    · O percentual de mulheres solteiras >>> {porcentagem_mulheres_solteiras}%
    · A quantidade de mulheres divorciadas acima de 30 anos >>> {quantidade_de_mulheres_divorciadas} MULHER


""")

        

        
        







main()