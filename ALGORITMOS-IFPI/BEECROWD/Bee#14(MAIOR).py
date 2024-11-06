num_1 = int(input('Qual o primeiro numero: '))
num_2 = int(input('Qual o segundo numero: '))
num_3 = int(input('Qual o tereceiro numero: '))

maior_ab = (num_1 + num_2 + abs(num_1 - num_2)) / 2
maior_entre_todos = (maior_ab + num_3 + abs(maior_ab - num_3)) / 2


print(f'{int(maior_entre_todos)} eh o maior')