# 9. Leia LimiteSuperior e LimiteInferior e escreva todos os números pares entre os limites lidos.

def main():

    print("""
=====================================
>>>  NÚMEROS PARES ENTRE LIMITES <<<
=====================================
""")
    LimiteInferior = int(input('Informe um Limite Inferior: '))
    LimiteSuperior = int(input('Informe um Limite Superior: '))

    lista = [i for i in range(LimiteInferior, LimiteSuperior + 2)]
    filtro_pares = list(filter(lambda i: i % 2 == 0, lista))

    print (f"""
==================================================
>>> A ordem de números pares entre {LimiteInferior} e {LimiteSuperior} <<<
==================================================

>> {filtro_pares} <<
""")

# outra forma de fazer:

 # ordem = ''

    # for contador in range(LimiteInferior, LimiteSuperior + 2):

       # if contador % 2 == 0:

            # ordem = ordem + str(contador) + ' '

main()