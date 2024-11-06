# 15. Leia N, calcule e escreva os N primeiros termos de seqüência (1, 3, 6, 10, 15,...).


def main():

    numero_de_termos = int(input("Informe o número de termos da sequência: "))

    contador = 2
    valor = 1
    ordem = ""

    sequencia = ["1"]

    while contador <= numero_de_termos:
        
        valor += contador

        contador += 1

        sequencia.append(str(valor))

    ordem = ", ".join(sequencia)

    print("[",ordem,"]")

main()