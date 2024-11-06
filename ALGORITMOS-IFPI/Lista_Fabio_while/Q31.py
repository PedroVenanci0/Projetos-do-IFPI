# 31. Escreva um algoritmo que leia um número decimal (até 3 dígitos) e escreva o seu equivalente em
# numeração romana. Utilize funções para obter cada dígito do número decimal e para a transformação
# de numeração decimal para romana (Dica: 1 = I, 5 = V, 10 = X, 50 = L, 100 = C, 500 = D, 1.000 = M).


def main():
    
    numero = limites_min_max('', 1, 999)
    centena = isolando_centena(numero)
    dezena = isolando_dezena(numero)
    unidade = isolando_unidade(numero)

    centena_romana = para_romano(centena)
    dezena_romana = para_romano(dezena)
    unidade_romana = para_romano(unidade)

    numero_romano = centena_romana + dezena_romana + unidade_romana

    print(f'{numero_romano}')

def isolando_centena(numero):
    return (numero // 100) * 100

def isolando_dezena(numero):
    return ((numero % 100) // 10) * 10

def isolando_unidade(numero):
    return (numero % 10)

def para_romano(numero):
    if numero < 10:
        return unidade_para_romano(numero)
    elif numero < 100:
        return dezena_para_romano(numero)
    else:
        return centena_para_romano(numero)

def unidade_para_romano(numero):
    if numero == 1:
        return "I"
    elif numero == 2:
        return "II"
    elif numero == 3:
        return "III"
    elif numero == 4:
        return "IV"
    elif numero == 5:
        return "V"
    elif numero == 6:
        return "VI"
    elif numero == 7:
        return "VII"
    elif numero == 8:
        return "VIII"
    elif numero == 9:
        return "IX"
    else:
        return ""

def dezena_para_romano(numero):
    if numero == 10:
        return "X"
    elif numero == 20:
        return "XX"
    elif numero == 30:
        return "XXX"
    elif numero == 40:
        return "XL"
    elif numero == 50:
        return "L"
    elif numero == 60:
        return "LX"
    elif numero == 70:
        return "LXX"
    elif numero == 80:
        return "LXXX"
    elif numero == 90:
        return "XC"
    else:
        return ""

def centena_para_romano(numero):
    if numero == 100:
        return "C"
    elif numero == 200:
        return "CC"
    elif numero == 300:
        return "CCC"
    elif numero == 400:
        return "CD"
    elif numero == 500:
        return "D"
    elif numero == 600:
        return "DC"
    elif numero == 700:
        return "DCC"
    elif numero == 800:
        return "DCCC"
    elif numero == 900:
        return "CM"
    else:
        return ""

def limites_min_max(mensagem, min, max):
    numero = int(input(mensagem))
    if numero < min or numero > max:
        print('Número inválido! Digite novamente')
        return limites_min_max(mensagem, min, max)
    return numero

main()
