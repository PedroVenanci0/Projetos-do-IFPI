# 26. Cada espectador de um cinema respondeu a um questionário no qual constava sua idade e a sua opinião
# em relação ao filme (1=ótimo, 2=bom, 3=regular, 4=péssimo). Escreva um algoritmo que leia a idade e
# a opinião das pessoas, calcule e mostre ao final: (FLAG: idade = -1).
# · a média das idades das pessoas que responderam ótimo;
# · a quantidade de pessoas que respondeu regular;
# . o percentual de pessoas que respondeu bom entre os entrevistados.

def main():

    contador_pessoas_regular = 0
    contador_pessoas_otimo = 0 
    contador_pessoas_total = 0
    idade_pessoas_otimo = 0 
    contador_pessoas_bom = 0

    print (""">>>> QUESTIONÁRIO SOBRE O FILME <<<<""")


    idade = int(input('Informe sua idade: '))
    opiniao = int(input('Informe sua opiniao em relação ao filme (1=ótimo, 2=bom, 3=regular, 4=péssimo): '))

    while (idade != (-1)):

        if opiniao == 1:

            contador_pessoas_otimo += 1
            idade_pessoas_otimo += idade

        if opiniao == 3:

            contador_pessoas_regular += 1
        
        if opiniao == 2:

            contador_pessoas_bom += 1
        
        contador_pessoas_total += 1
    
        idade = int(input('Informe sua idade: '))

        if idade != (-1):

            opiniao = int(input('Informe sua opiniao em relação ao filme (1=ótimo, 2=bom, 3=regular, 4=péssimo): '))
        
    
    media_idade_otimo = (idade_pessoas_otimo / contador_pessoas_otimo)
    percentual_opniao_bom = (contador_pessoas_bom * 100) / contador_pessoas_total


    print (f"""
           
            >>>> RESULTADOS <<<<
           -----------------------
           
           . MÉDIA DE PESSOAS QUE RESPONDERAM ÓTIMO >>> {media_idade_otimo}
           . PERCENTUAL DE PESSOAS QUE RESPONDERAM BOM >>> {percentual_opniao_bom}
           . QUANTIDADE DE PESSOAS QUE RESPONDERAM REGULAR >>> {contador_pessoas_regular}

""")  


            





main()