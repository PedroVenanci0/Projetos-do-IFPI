nome = input('')
salaio_fixo = float(input(''))
total_vendas = float(input(''))

comissao = total_vendas * 15/100

total = comissao + salaio_fixo


print (f'TOTAL = R$ {total:.2f}')