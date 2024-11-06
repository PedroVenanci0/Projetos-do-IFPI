
# [energia.js] Em 2021 o Brasil voltou a enfrentar crise na matriz energética devido ao baixo nível das águas nos reservatórios das hidrelétricas
# brasileiras. Devido a isso os consumidores deverão arcar com custos extras (bandeira) para bancar outras matrizes energéticas, como usinas
# termoelétricas. Neste mês de Junho a bandeira estabelecida pelo governo federal foi a Vermelha Patamar 2, que significa que a cada 100 KWh de
# consumo será acrescido uma taxa extra de R$ 8,00.

# O Cálculo da energia elétrica para o consumidor final é feito baseado em KWh e em faixas.
# Valores hipotéticos:
#   ● Consumo de até 30KWh isento de tarifa.
#   ● Até 100 KWh será cobrado R$ 0,59 por cada um cada de todo os KWh consumidos;
#   ● acima de 100KWh o valor de R$ 0,75 por cada um de todos os KWh consumidos.

# Sobre o valor tarifado/apurado são 25% de ICMS e 15% de PIS/CONFIS.

# A taxa de iluminação pública é cobrada apenas para os consumidores que passarem de 80KWh por mês, e custa 6% do valor tarifado (antes do
# impostos).

# Considerando os dados acima construa um software que receba dois dados:
# Leitura Atual e Leitura Anterior do medidor de energia e faça todo o cálculo do "Talão de Energia" conforme detalhado acima
# Como saída apresente os dados que compõem assim como o valor total a ser pago.

# Exemplo:
# Consumo 000 KWh
# Valor Faturado R$ 0,00
# Bandeira R$ 0,00 (x bandeiras)
# ICMS R$ 0,00
# PIS/CONFIS
# Taxa Iluminação R$ 0,00

from utils import clear_screen
def main():

    print ('\n============================================')
    print ('>>> CALCULANDO DADOS DO TALÃO DE ENERGIA <<<')
    print ('============================================\n')

    LeituraAtual = float(input('>>> Informe a leitura atual da medida de energia: '))
    LeituraAnterior = float(input('>>> Informe a leitura anterior da medida de energia: '))

    consumo_energia = abs(LeituraAnterior - LeituraAtual)

    taxa_de_ilumincao = 0

    valor_khw_sem_imposto = 0
  
    if consumo_energia <= 100 and consumo_energia > 30:

        valor_khw_sem_imposto = consumo_energia * 0.59

        if valor_khw_sem_imposto >= 80:

            taxa_de_ilumincao = calculando_taxa_iluminacao(valor_khw_sem_imposto)
            
        valor_khw_sem_imposto = taxa_de_ilumincao + valor_khw_sem_imposto

    elif consumo_energia > 100:

        valor_khw_sem_imposto = consumo_energia * 0.75

        taxa_de_ilumincao = calculando_taxa_iluminacao(valor_khw_sem_imposto)
        valor_khw_sem_imposto = taxa_de_ilumincao + valor_khw_sem_imposto

    imposto_Pis = (valor_khw_sem_imposto * (15/100))
    imposto_ICMs = (valor_khw_sem_imposto * (25/100))
    
    valor_khw_total = imposto_Pis + imposto_ICMs + valor_khw_sem_imposto

    numero_bandeiras = consumo_energia // 100

    valor_bandeiras = numero_bandeiras * 8

    if numero_bandeiras > 0:
         
        valor_khw_total = valor_bandeiras + valor_khw_total
    
    if consumo_energia <= 30:

            print ('\n\033[32m>>> O CONSUMIDOR ESTÁ ISENTO DE TARIFA <<<\033[m\n')
    else:
        clear_screen()
        print (f"""       
                            \033[33m>>>>>>    TALÃO DE ENERGIA    <<<<<<\033[m
    \033[33m===========================================================================================\033[m
        . Consumo                       >> {consumo_energia} KWh
        . Valor Faturado                >> R$ {valor_khw_total}
        . Bandeira                      >> R$ {valor_bandeiras} ({numero_bandeiras} bandeiras)
        . ICMS                          >> R$ {imposto_ICMs} 
        . PIS/CONFIS                    >> R$ {imposto_Pis}
        . Taxa Iluminação               >> R$ {taxa_de_ilumincao}
    \033[33m===========================================================================================\033[m

""")

def calculando_taxa_iluminacao(valor_khw_sem_imposto):

        taxa_de_ilumincao = (valor_khw_sem_imposto * (6/100))

        return taxa_de_ilumincao



main()
