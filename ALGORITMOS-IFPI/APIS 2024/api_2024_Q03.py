# [q3_media] Faça um programa para auxílio o Prof. Joaquim ter
# dados sobre rendimento numa avaliação que aplicou a seus
# aluno. O professor irá digitar as notas de seus alunos e você deve
# computar: Maior Nota Geral, Menor Nota Geral, Média Geral da
# turma,. Performance das Notas dos Homens(escala 0 a 100%),
# Performance das Mulheres (escala 0 a 100%). A entrada será
# Sexo (M ou F) e Nota (número entre 1 e 10). Encerra quando sexo
# for diferente de M e F. Mostre quanto alunos, quantos de cada
# sexo, também. Classifique o desempenho da turma, e também
# homens e mulheres, em:

# a. Péssimo [0 a 2]
# b. Ruim ]2 a 4]
# c. Regular [4 a 6[
# d. Bom [6 a 8[
# e. Excelente [8 a 10

from utils import clear_screen

def main():
    print("""
================================================
>>> Analise do rendimento dos alunos de ADS <<<
================================================
""")
    
    print("""
======================================
            1°  ALUNO
======================================
""")
    
    sexo_aluno = input('Informe o sexo do alun@ (M/F)\n>> ').upper()
    nota_aluno = int(input('Informe a nota do alun@(1 a 10)\n>> '))

    maior_nota = nota_aluno
    menor_nota = nota_aluno

    numero_alunos = 1

    somatorio_notas = nota_aluno
    somatorio_notas_masculinas = 0
    somatorio_notas_femenina = 0

    desempenho_masculino = ''
    desempenho_femenino = ''

    aluno_femenina = 0
    aluno_masculino = 0

    if sexo_aluno == "M":
        aluno_masculino += 1
        somatorio_notas_masculinas += nota_aluno

    elif sexo_aluno == "F":
        aluno_femenina += 1
        somatorio_notas_femenina += nota_aluno
    
    while sexo_aluno == "M" or sexo_aluno == "F":

        print(f"""
======================================
            {numero_alunos + 1}°  ALUNO
======================================
""")

        sexo_aluno = input('Informe o sexo do alun@\n>> ').upper()

        if sexo_aluno == "M" or sexo_aluno == "F":

            nota_aluno = int(input('Informe a nota do alun@(1 a 10)\n>> '))

            if nota_aluno > maior_nota: 
                maior_nota = nota_aluno

            elif nota_aluno < menor_nota:
                menor_nota = nota_aluno

            if sexo_aluno == "M":
                aluno_masculino += 1
                somatorio_notas_masculinas += nota_aluno

            elif sexo_aluno == "F":
                aluno_femenina += 1
                somatorio_notas_femenina += nota_aluno
            
            somatorio_notas += nota_aluno
            numero_alunos += 1

    media_da_turma = somatorio_notas / numero_alunos

    performance_maculina = (somatorio_notas_masculinas / aluno_masculino) 
    performance_femenina = (somatorio_notas_femenina / aluno_femenina) 

    desempenho_masculino = calculando_desempenho(performance_maculina)
    desempenho_femenino = calculando_desempenho(performance_femenina)
    desempenho_geral = calculando_desempenho(media_da_turma)

    clear_screen()
    print(f"""
===============================================
    >>> RESULTADO DAS AVALIAÇÕES DE ADS <<<
===============================================
. NÚMERO DE ALUNOS      >> {numero_alunos}
. NÚMERO DE ALUNOS (M)  >> {aluno_masculino}
. NÚMERO DE ALUNOS (F)  >> {aluno_femenina}
===============================================
. MAIOR NOTA GERAL      >> {maior_nota}
. MENOR NOTA GERAL      >> {menor_nota}
. MÉDIA GERAL           >> {media_da_turma}
===============================================
. PERFORMANCE (M)       >> {performance_maculina * 10}%
. PERFORMANCE (F)       >> {performance_femenina * 10}%
===============================================
. DESEMPENHO (M)        >> {desempenho_masculino}
. DESEMPENHO (F)        >> {desempenho_femenino}
. DESEMPENHO GERAL      >> {desempenho_geral}
===============================================
""")

def calculando_desempenho(media):

    if media <= 2:
        desempenho = "\033[31mPÉSSIMO\033[m"
        return desempenho
        
    elif media > 2 and media <= 4:
        desempenho = "\033[35mRUIM\033[m"
        return desempenho
        
    elif media > 4 and media <= 6:
        desempenho = "\033[34mREGULAR\033[m"
        return desempenho
        
    elif media > 6 and media <= 8:
        desempenho = "\033[36mBOM\033[m"
        return desempenho
        
    elif media > 8 and media <= 10:
        desempenho = "\033[32mEXCELENTE\033[m"
        return desempenho

main()