# 11. Leia informações de alunos (matrícula, nota1, nota2, nota3) com o fim das informações indicado por
# matrícula = 0. Para cada aluno deve ser calculada a média final de acordo com a seguinte fórmula:

# Média Final = ((2 * nota1) + (3 * nota2) + (5 * nota3)) / 10

# Se a média final for igual ou superior a 7, o aluno está aprovado; se a média final for inferior a 7, o
# aluno está reprovado. Ao final devem ser mostrados o total de aprovados, o total de reprovados e o total
# de alunos da turma.

def main():

    matricula = ''

    contador_alunos = 0
    aluno_aprovado = 0
    aluno_reprovado = 0

    while (matricula != 0):

        matricula = int(input('Informe a matrícula do aluno: '))

        if (matricula != 0):

            nota_01 = float(input('informe a primeira nota do aluno: '))
            nota_02 = float(input('informe a segunda nota do aluno: '))
            nota_03 = float(input('informe a terceira nota do aluno: '))

            media_final = ((2 * nota_01) + (3 * nota_02) + (5 * nota_03)) / 10

            if media_final >= 7:

                aluno_aprovado += 1
        
            else:
                aluno_reprovado += 1

            contador_alunos += 1



    print (f' TOTAL DE APROVADOS: {aluno_aprovado}')
    print (f' TOTAL DE REPROVADOS: {aluno_reprovado}')
    print (f' TOTAL DE ALUNOS: {contador_alunos}')
        





main()