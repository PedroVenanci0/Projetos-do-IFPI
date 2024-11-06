
def main():

    segundos_totais_iniciais = int(input())

    convertendo = segundos_totais_iniciais // 60
    horas = convertendo // 60
    minutos = convertendo % 60
    segundos = (((horas * 60) * 60) + (minutos * 60)) - segundos_totais_iniciais

    print(f'{horas}:{minutos}:{abs(segundos)}')

main()