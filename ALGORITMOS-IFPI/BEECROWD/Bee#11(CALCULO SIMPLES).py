
peças_01 = int(input('Qual o codigo1: ')), int(input('Numero de peças1: ')), float(input('valor unitario1: '))
peças_02 = int(input('Qual o codigo2: ')), int(input('Numero de peças2: ')), float(input('valor unitario2: '))

valor_total = ((peças_01[1] * peças_01[2]) + (peças_02[1] * peças_02[2]))

print(f'VALOR A PAGAR: R$ {valor_total:.2f}')