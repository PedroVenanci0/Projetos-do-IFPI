def main():

    numero_linhas = int(input())

    todos_resultados = []

    for elements in range(numero_linhas):

        text_code = input()

        posições_alteradas = primeiro_passo(text_code)
        invertido = segundo_passo(posições_alteradas)
        mover_posição_ASCII = terceiro_passo(invertido)

        resultado = mover_posição_ASCII

        todos_resultados.append(resultado)

    for elements in todos_resultados:
        print(elements)


def primeiro_passo(text_code):

    posições_alteradas = ''

    for elements in range(len(text_code)):

        char = text_code[elements]

        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
           
            posições_alteradas += chr(ord(char) + 3)

        elif '0' <= char <= '9':
            posições_alteradas += chr(ord(char))

        else:
            posições_alteradas += chr(ord(char))

    
    return posições_alteradas


def segundo_passo(texto_codificado):

    texto_invertido = ''

    for elements in range(len(texto_codificado)-1, -1, -1):
        texto_invertido += texto_codificado[elements]
    
    
    return texto_invertido

def terceiro_passo(texto_invertido):

    meio_da_string_truncado = len(texto_invertido) // 2
    texto_codificado = ""

    for elements in range(len(texto_invertido)):

        texto_invertido[elements]

        if elements >= meio_da_string_truncado:
            texto_codificado += chr(ord(texto_invertido[elements]) - 1)

        else:
            texto_codificado += texto_invertido[elements]

    return texto_codificado

main()