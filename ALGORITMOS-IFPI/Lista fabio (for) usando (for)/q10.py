# 10. Leia LimiteSuperior e LimiteInferior e escreva todos os números ímpares entre os limites lidos.

def main():

    print("""
=====================================
>>>  NÚMEROS PARES ENTRE IMPARES <<<
=====================================
""")

    LimiteInferior = int(input('Informe um Limite Inferior: '))
    LimiteSuperior = int(input('Informe um Limite Superior: '))

    lista = [i for i in range(LimiteInferior, LimiteSuperior + 1)]
    filtro_impares = list(filter(lambda i: i % 2 != 0, lista))
        
    print (f"""
==================================================
>>> A ordem de números ímpares entre {LimiteInferior} e {LimiteSuperior} <<<
==================================================

>> {filtro_impares} <<
""")

main()

#ordem = ''

    #for contador in range(LimiteInferior, LimiteSuperior):

        #if contador % 2 != 0:

            #   ordem = ordem + str(contador) + " "