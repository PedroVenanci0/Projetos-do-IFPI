# . [q1_senha] Atualmente precisamos em vários momentos criar
# senhas numéricas para acesso a serviços diversos. Muitos
# sistemas têm políticas de senha, evitando assim senhas comuns
# como por exemplo: 123456, ou 223344.
# Seu objetivo portanto é fazer um Gerador de Senhas com as
# seguintes regras:
# - Numérica com tamanho fixo de N dígitos
# - Não deve permitir que o digital atual seja igual ao anterior
# - Não pode também ser antecessor ou sucessor imediato.
# - O usuário vai pedir uma senha, e então você deve mostrar a
# senha sugerida seguindo as regras.
# - E então perguntar se ele está satisfeito com a senha
# gerada. Caso negativo, g

import random

def main():

    print("""
===================================
    >>> GERADOR DE SENHAS <<<
===================================
""")

    numero_de_digitos_senha = int(input('>> Informe o número de digitos da senha: '))

    senha = ""
    flag = "N"
    numero_aleatorio_posterior = 0
    numero_aleatorio_anterior = 0

    while flag != "Y":

        while len(senha) != numero_de_digitos_senha:


            numero_aleatorio = random.randint(1,9)

            numero_aleatorio_posterior = numero_aleatorio

            if (numero_aleatorio != numero_aleatorio - 1) and (numero_aleatorio != numero_aleatorio + 1) and (numero_aleatorio_posterior != numero_aleatorio_anterior):

                senha = senha + str(numero_aleatorio)

            numero_aleatorio_anterior = numero_aleatorio_posterior
    
        print(f'\n>> A senha gerada: {senha}\n')

        flag = input('>> Está satisfeito com a senha gerada(y/n)? ').upper()

        if flag != "Y":
            senha = ""
        
    print(f'\n>> SENHA {senha} APROVADA COM SUCESSO!!\n')
        
main()