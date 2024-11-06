def main():

    valor = float(input())

    valor_centavos = int(valor * 100)

    contador_nota_100 = valor_centavos // 10000
    valor_centavos %= 10000

    contador_nota_50 = valor_centavos // 5000
    valor_centavos %= 5000

    contador_nota_20 = valor_centavos // 2000
    valor_centavos %= 2000

    contador_nota_10 = valor_centavos // 1000
    valor_centavos %= 1000

    contador_nota_5 = valor_centavos // 500
    valor_centavos %= 500

    contador_nota_2 = valor_centavos // 200
    valor_centavos %= 200

    contador_moeda_1 = valor_centavos // 100
    valor_centavos %= 100

    contador_moeda_50 = valor_centavos // 50
    valor_centavos %= 50

    contador_moeda_25 = valor_centavos // 25
    valor_centavos %= 25

    contador_moeda_10 = valor_centavos // 10
    valor_centavos %= 10

    contador_moeda_5 = valor_centavos // 5
    valor_centavos %= 5

    contador_moeda_01 = valor_centavos

    print('NOTAS:')
    print(f'{contador_nota_100} nota(s) de R$ 100.00')
    print(f'{contador_nota_50} nota(s) de R$ 50.00')
    print(f'{contador_nota_20} nota(s) de R$ 20.00')
    print(f'{contador_nota_10} nota(s) de R$ 10.00')
    print(f'{contador_nota_5} nota(s) de R$ 5.00')
    print(f'{contador_nota_2} nota(s) de R$ 2.00')
    print('MOEDAS:')
    print(f'{contador_moeda_1} moeda(s) de R$ 1.00')
    print(f'{contador_moeda_50} moeda(s) de R$ 0.50')
    print(f'{contador_moeda_25} moeda(s) de R$ 0.25')
    print(f'{contador_moeda_10} moeda(s) de R$ 0.10')
    print(f'{contador_moeda_5} moeda(s) de R$ 0.05')
    print(f'{contador_moeda_01} moeda(s) de R$ 0.01')

main()
