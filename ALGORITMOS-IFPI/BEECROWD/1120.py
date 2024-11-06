def main():

    while True:
    
        digito_falho, informe_o_valor = map(str, input().split())

        if digito_falho == "0" and informe_o_valor == "0":
            break

        digito_formatado = ""
        valor_correto = 0

        for elements in informe_o_valor:
            if elements != digito_falho:
                digito_formatado += elements
        
        if digito_formatado == '':
            valor_correto = 0

        else:
            valor_correto = int(digito_formatado)

        print(valor_correto)

main()