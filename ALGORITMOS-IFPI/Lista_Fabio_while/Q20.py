# 20. Considere que um carro vai fazer uma viagem entre duas cidades e que a distância a ser percorrida é de
# 600 km. No início da viagem, o carro está com o tanque cheio (50 litros). Durante o percurso foi usado
# um aparelho para medir o desempenho do carro, que mostrava, quando acionado, duas informações:
# · Distância percorrida desde a última medição;
# · Quantidade de litros consumidos para percorrer a distância indicada.

#     Escreva um algoritmo que leia estas informações e escreva:
# · se o carro chegou ao seu destino (distância percorrida maior ou igual a 600 km);
# · se o carro parou antes de chegar por falta de combustível (consumo igual a 50 litros);
# · o consumo em km/l do carro.

def main():

    distancia_percorrida = float(input('Informe a distancia percorrida des a ultima medição: '))
    litros_gastos_por_distancia = float(input('A quantidade de litros consumidos para percorrer a distância indicada: '))

    distancia_ao_fim_da_viagem = 600
    qnt_de_combustivel_no_tanque = 50
    km_por_litro = distancia_percorrida / litros_gastos_por_distancia

    while distancia_percorrida < distancia_ao_fim_da_viagem and qnt_de_combustivel_no_tanque > 0:

        distancia_ao_fim_da_viagem -= distancia_percorrida
        qnt_de_combustivel_no_tanque -= litros_gastos_por_distancia

    if qnt_de_combustivel_no_tanque <= 0:

        print ('o carro parou antes de chegar por falta de combustível')
        print (f'O consumo do carro foi de {km_por_litro} km/l')

    elif distancia_percorrida >= distancia_ao_fim_da_viagem:

        print ('o carro chegou ao seu destino')
        print (f'O consumo do carro foi de {km_por_litro} km/l')

    


    


        

        







main()