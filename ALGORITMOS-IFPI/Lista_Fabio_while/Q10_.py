# 10. Calcule a quantidade de combustível que pode ser colocada em uma aeronave e verifique se a aeronave
# pode levantar vôo ou não. Considere os seguintes critérios:

# · O peso de decolagem da aeronave é sempre igual a 500.000 kg;
# · O peso de decolagem é composto pela soma do peso do combustível, do peso da carga, do peso dos passageiros;
# · O peso do combustível é a quantidade do combustível (em litros) multiplicada pelo fator 1.5kg/l;
# · A quantidade mínima de combustível para que a aeronave decole é de 10000 l;
# · O peso da carga é o somatório do peso dos “containers” de cargas em quilogramas.
# · O peso dos passageiros é o somatório do peso de cada passageiro e de todos os volumes da sua
# bagagem; cada passageiro tem o peso estimado de 70kg e cada volume de bagagem tem o peso estimado de 10kg.

# O algoritmo deve ler o números de containers e a seguir ler o peso de cada container. A seguir devem
# ser lidos os dados dos passageiros (número do bilhete, quantidade de bagagens) até que o número do
# bilhete seja igual a 0. Devem ser mostrados, a quantidade de passageiros, a quantidade total de volume
# de bagagem, o peso dos passageiros, o peso da carga, a quantidade possível de combustível, e uma
# mensagem indicando a liberação da decolagem ou não.

def main():

    containers = int(input('Informe o número de containers: '))
    
    contador_containers = 0
    peso_total_containers = 0

    while (contador_containers != containers):

        peso = float(input('Informe o peso do containers: '))

        peso_total_containers = peso + peso_total_containers

        contador_containers += 1

    bilhete = int(input('Informe o numero do bilhete: '))

    passageiros = 0
    total_bagagens = 0
    
    while bilhete != 0:

        quantidade_bagagens = int(input('Informe a quantidade de bagagens: '))

        total_bagagens = quantidade_bagagens + total_bagagens

        passageiros += 1

        bilhete = int(input('Informe o numero do bilhete: '))

    peso_total_passageiros = (passageiros * 70) + (total_bagagens * 10)

    quantidade_combutivel_kg = 500_000 - (peso_total_passageiros + peso_total_containers) 

    quantidade_combutivel_Litros = quantidade_combutivel_kg * 1.5

    if quantidade_combutivel_Litros <= 10_000:

        decolagem = ('NÃO FOI AUTORIZADA!!!')
    else: 

        decolagem = ('FOI AUTORIZADA!!!')
    
    print (f'--->   Quantidade de passageiros: {passageiros}')
    print (f'--->   Quantidade de BAGAGENS: {total_bagagens}')
    print (f'--->   O peso total dos passageiros é {peso_total_passageiros}')
    print (f'--->   O peso total dos containers é {peso_total_containers}')
    print (f'--->   Quantidade possivel de combustivel {quantidade_combutivel_kg}')
    print (f'--->   A decolagem do avião {decolagem}')




    




main()