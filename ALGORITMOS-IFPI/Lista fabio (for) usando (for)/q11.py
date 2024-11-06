# 11. Leia LimiteSuperior e LimiteInferior e escreva todos os números primos entre os limites lidos.

def main():

    print("""
========================================
>>> NÚMEROS PRIMSO DENTRO DOS LIMTES <<<
========================================
""")

    LimiteInferior = int(input('>> Informe um Limite Inferior: '))
    LimiteSuperior = int(input('>> Informe um Limite Superior: '))


    ordem_de_primos = verificando_ordem(LimiteInferior, LimiteSuperior)

    print (ordem_de_primos)

    
    
def numeros_primos(LimiteInferior, LimiteSuperior):

    ordem = ''

    for contador in range(LimiteInferior, LimiteSuperior):

        if contador % 2 != 0 and contador % 3 != 0 and contador % 5 != 0 and contador % 7 != 0:

            if contador == 1:

                contador = ''

            ordem = ordem + str(contador) + " "

    return ordem

def verificando_ordem(LimiteInferior, LimiteSuperior):

    if LimiteInferior > 7:

        lista_primos = numeros_primos(LimiteInferior, LimiteSuperior)

        return (f"""
======================================================
>>> A ordem de números primos entre {LimiteInferior} e {LimiteSuperior} <<<
======================================================

>> {lista_primos} << 
""")
    
    elif LimiteInferior <= 2:

        lista_primos = numeros_primos(LimiteInferior, LimiteSuperior)

        return (f"""
================================================                
>>> A ordem de números primos entre {LimiteInferior} e {LimiteSuperior} <<<
================================================

>> {'2 3 5 7' + " " + str(lista_primos)} <<
""")

    elif LimiteInferior == 3:
        lista_primos = numeros_primos(LimiteInferior, LimiteSuperior)

        return (f"""
================================================                
>>> A ordem de números primos entre {LimiteInferior} e {LimiteSuperior} <<<
================================================

>> {'3 5 7' + " " + str(lista_primos)} <<
""")

    elif LimiteInferior == 4:

        lista_primos = numeros_primos(LimiteInferior, LimiteSuperior)

        return (f"""
================================================                
>>> A ordem de números primos entre {LimiteInferior} e {LimiteSuperior} <<<
================================================

>> {'5 7' + " " + str(lista_primos)} <<
""")

    elif LimiteInferior == 5:

        lista_primos = numeros_primos(LimiteInferior, LimiteSuperior)

        return (f"""
================================================                
>>> A ordem de números primos entre {LimiteInferior} e {LimiteSuperior} <<<
================================================

>> {'5 7' + " " + str(lista_primos)} <<
""")

    elif LimiteInferior == 6:

        lista_primos = numeros_primos(LimiteInferior, LimiteSuperior)

        return (f"""
================================================                
>>> A ordem de números primos entre {LimiteInferior} e {LimiteSuperior} <<<
================================================

>> {'7' + " " + str(lista_primos)} <<
""")

    elif LimiteInferior == 7:

        lista_primos = numeros_primos(LimiteInferior, LimiteSuperior)

        return (f"""
================================================                
>>> A ordem de números primos entre {LimiteInferior} e {LimiteSuperior} <<<
================================================

>> {'7' + " " + str(lista_primos)} <<
""")

main()

# uma forde fazer sem os números 2,3,5,7

#lista = [i for i in range(LimiteInferior, LimiteSuperior)]
 #   filtro_primos = list(filter(lambda i: i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0, lista))

  #  return filtro_primos