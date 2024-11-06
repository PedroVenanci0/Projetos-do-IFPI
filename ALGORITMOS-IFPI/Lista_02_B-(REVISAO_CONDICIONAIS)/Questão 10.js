/**10. Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a
sua média. A atribuição de conceitos obedece à tabela abaixo:
Média de Aproveitamento Conceito
Entre 9.0 e 10.0 A
Entre 7.5 e 9.0 B
Entre 6.0 e 7.5 C
Entre 4.0 e 6.0 D
Entre 4.0 e zero E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem
“APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E. */

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Média de Aproveitamento #### ")

function main(){

    // Entrada

    const nota_01 = get_number("Informe sua primeira nota: ")
    const nota_02 = get_number("Informe sua segunda nota: ")

    // Processamento

    const situacao_escolar = calculando_media(nota_01, nota_02)

    // Saida

    console.log (situacao_escolar)


}

function calculando_media(nota_01, nota_02){

    const media = (nota_01 + nota_02) / 2

    if (media > 9 && media <= 10){

        return (`

        -----------------
    
        BOLETIM:
        Nota 1: ${nota_01}
        Nota 2: ${nota_02}

        -----------------

        Média: ${media}

        -----------------

        Situação: APROVADO COM GRATULAÇÃO A
        
        
        `)

    }
    else if (media > 7.5 && media <= 9){

        return (`

        -----------------
    
        BOLETIM:
        Nota 1: ${nota_01}
        Nota 2: ${nota_02}

        -----------------

        Média: ${media}

        -----------------

        Situação: APROVADO COM GRATULAÇÃO B
        
        
        `)

    }
    else if (media > 6 && media <= 7.5 ){

        return (`
        
        BOLETIM:
        Nota 1: ${nota_01}
        Nota 2: ${nota_02}

        -----------------

        Média: ${media}

        -----------------

        Situação: APROVADO COM GRATULAÇÃO C
        
        
        `)
    }
    else if (media > 4 && media <= 6){

        return (`

        -----------------
    
        BOLETIM:
        Nota 1: ${nota_01}
        Nota 2: ${nota_02}

        -----------------

        Média: ${media}

        -----------------

        Situação: REPROVADO COM GRATULAÇÃO D
        
        
        `)
    }
    else if (media > 0 && media <= 4){

        return (`

        -----------------
    
        BOLETIM:
        Nota 1: ${nota_01}
        Nota 2: ${nota_02}

        -----------------

        Média: ${media}

        -----------------

        Situação: REPROVADO COM GRATULAÇÃO E
        
        
        `)
    }
}

main()