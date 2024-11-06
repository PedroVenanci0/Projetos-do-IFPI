
# 8. Leia N , LimiteSuperior e LimiteInferior e escreva todos os múltiplos de N entre os limites lidos.

def main():

    print("""
\n=================================
>>>  MULTIPLOS ENTRE LIMITES <<<
=================================\n
""")
    # Entrada

    multiplos_do_numero = int(input('Informe o número do qual iremos procurar seus multiplos: '))
    LimiteInferior = int(input('Informe um Limite Inferior: '))
    LimiteSuperior = int(input('Informe um Limite Superior: '))

    # PROCESSAMENTO

    lista = [i for i in range(LimiteInferior, LimiteSuperior + multiplos_do_numero)]
    filtro_multiplo = list(filter(lambda i: i % multiplos_do_numero == 0, lista))

    # DESCOBRINDO O NUMERO DE "=" PARA ESTETIZAR A SAIDA :)
    numero_de_espaços = len(f'A ordem de números multiplos de {multiplos_do_numero} entre {LimiteInferior} e {LimiteSuperior} é {filtro_multiplo}') * "="

    # SAIDA 
    print (f"""
{numero_de_espaços}
A ordem de números multiplos de {multiplos_do_numero} entre {LimiteInferior} e {LimiteSuperior} é {filtro_multiplo}
{numero_de_espaços}

""")
    
    # outra forma de fazer
 # ordem = ''
    # for contador in range(LimiteInferior, (LimiteSuperior + numero_N)):       
        # ordem = ordem + str(contador) + " "

main()