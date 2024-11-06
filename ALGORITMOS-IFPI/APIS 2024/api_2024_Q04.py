# [q4_viagem] José está planejando uma viagem com sua família
# para a Capital Federal. Para isso tem juntado Milhas em
# programas de fidelidade, e também pesquisando passagens
# aéreas diretamente. No Programa Smiles é possível comprar
# Milhas Aéreas pagando 70 reais a cada 1000 unidades. Uma
# passagem Teresina(THE) para Brasília(BSB) custa em torno de
# 21200 milhas, o mesmo voo(horário) tá por R$ 431. Ou seja,
# nesse caso, é melhor comprar em R$ que comprar Milhas a R$
# 70/Milheiro para então emitir o Voo.

# Entretanto no mundo das milhas, nunca compramos milhas a esse
# valor de 70 reais por mil, o que se faz é acumular milhas por meio
# de Cartão de Crédito e Compras Bonificadas. Neste caso,
# precifica-se as Milhas (valor convencionado) como baratas a R$
# 14,50 o Milheiro. Assim, o voo exemplificado acima as 21200
# Milhas custariam em reais o total de R$ 307,40. Desta forma,
# sendo vantajoso, ou seja, custa apena 71,3% do valor em R$
# normal (R$ 431)

# Faça um programa para auxiliar José no comparativo dos valor
# das passagens com Milhas Padrão(R$ 70), Milhas Acumuladas
# Baratas (R$ 14,50) e em Reais Normal (valor do site). 
# Peça ao usuário Origem, Destino, Valor em R$ no site e Valor em Milhas no Site. 
# Apresente para ele o valor equivalente em R$ caso compre
# com Milhas Padrão, indicando o % em relação ao valor em R$.
# Faça o mesmo para Milhas Baratas. Ao final, indique para ele a
# melhor forma de compra dentre as 3 opções.

def main():

    # Entrada

    print("""
============================================
  >>> PROGRAMANDO A VIAGEM DOS SONHOS <<<
============================================
""")
    
    origem = input('> Qual o local de partida: ').upper()
    destino = input('> Qual o destino final: ').upper()
    valor_passagem = float(input('> Informe o valor da passagem: '))
    quantidade_milhas = float(input('> Informe o valor dem milhas para se realizar a viagem: '))

    # Processamento

    milhas_padrao = 70
    milhas_baratas = 14,50
    
    numero_de_vezes_será_pago = quantidade_milhas / 1000

    preço_milhas_padrao = milhas_padrao * numero_de_vezes_será_pago
    preço_milhas_baratas = milhas_baratas * numero_de_vezes_será_pago

    lista_de_preços = menor_PREÇO(preço_milhas_baratas, preço_milhas_padrao, valor_passagem)

    porcentagem_valor_padrao = (preço_milhas_padrao * 100) / valor_passagem
    porcentagem_valor_barata = (preço_milhas_baratas * 100) / valor_passagem

    # Saida 

    print(f"""
======================================================================================================
                            >>>  TABELA DE PREÇOS (PASSAGENS) <<<
======================================================================================================
. VALOR DA PASSAGEM                     >> \033[32m{valor_passagem}\033[m R$
. VALOR A SE PAGAR COM MILHAS PADRÃO    >> \033[32m{preço_milhas_padrao}\033[m R$, OU SEJA, CUSTA APENAS {porcentagem_valor_padrao:.2f}% DO VALOR DA PASSAGEM
. VALOR A SE PAGAR COM MILHAS BARATAS   >> \033[32m{preço_milhas_baratas}\033[m R$, OU SEJA, CUSTA APENAS {porcentagem_valor_barata:.2f}% DO VALOR DA PASSAGEM
======================================================================================================
>>> É RECOMENDADO A COMPRA \033[34m{lista_de_preços}\033[m, PARA A REALIZAÇÃO DA VIAGEM DE {origem} ATÉ {destino}
======================================================================================================

""")

def menor_PREÇO(preco_01,preco_02, preco_03):

    menor_numero = preco_01 

    if preco_02 < preco_01 and preco_02 < preco_03:
        menor_numero = preco_02
        return "DA MILHA PADRÃO"

    if preco_03 < preco_01 and preco_03 < preco_02:
        menor_numero = preco_02
        return "DO VALOR DA PASSAGEM"
    
    return "DA MILHA BARATA"

   
main()
