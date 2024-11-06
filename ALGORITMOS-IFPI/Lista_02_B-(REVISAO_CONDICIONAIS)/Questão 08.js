/**8. Para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que
depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
11% do salário bruto, mas não é descontado (é a empresa que deposita). O salário líquido corresponde
ao salário bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a
quantidade de horas trabalhadas no mês.
Desconto do IR:
o Salário Bruto até R$ 900,00 (inclusive) - isento
o Salário Bruto até R$ 1.500,00 (inclusive) - desconto de 5%
o Salário Bruto até R$ 2.500,00 (inclusive) - desconto de 10%
o Salário Bruto acima de R$ 2.500,00 - desconto de 20%
Escreva na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e
a quantidade de hora é 220.
Salário Bruto: (5 * 220) : R$ 1100,00
(-) IR (5%) : R$ 55,00
(-) INSS ( 10%) : R$ 110,00
FGTS (11%) : R$ 121,00
Total de descontos : R$ 165,00
Salário Liquido : R$ 935,00 */


import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Folha de Pagamento #### ")

function main(){

    // Entrada 

    const hora_trabalho = get_number("Informe a quantidade de horas trabalhadas por mês: ")
    const valor_hora = get_number("Informe o valor da hora trabalhada: ")

    // processamento 

    const salario_liquido_definitivo = calculando_salario_liquido(hora_trabalho, valor_hora)

    // Saida 

    console.log (salario_liquido_definitivo)


}

function calculando_salario_liquido(hora_trabalho, valor_hora){

    const salario_bruto = hora_trabalho * valor_hora

    const INSS = salario_bruto * 10/100

    const FGTS = salario_bruto * 11/100



    if (salario_bruto <= 900){

        const salario_liquido = salario_bruto - INSS

        return (`

        . Salário Bruto (${hora_trabalho} * ${valor_hora}) = R$ ${salario_bruto}

        . (-) IR (isento)

        . (-) INSS ( 10% ): R$ ${INSS}

        . FGTS (11 %): R$ ${FGTS}

        . Total de descontos: R$ ${INSS}

        . Salário Liquido : R$ ${salario_liquido}


        
        
        `)

    }
    else if (salario_bruto > 900 && salario_bruto <= 1500){

        const IR = salario_bruto * 5/100

        const INSS = salario_bruto * 10/100

        const desconto_total = INSS + IR

        const salario_liquido = (salario_bruto - INSS) - IR


        return (`

        . Salário Bruto (${hora_trabalho} * ${valor_hora}) = R$ ${salario_bruto}

        . (-) IR (5%): R$ ${IR}

        . (-) INSS ( 10% ): R$ ${INSS}

        . FGTS (11 %): R$ ${FGTS}

        . Total de descontos: R$ ${desconto_total}

        . Salário Liquido : R$ ${salario_liquido}

        
        `)

    }
    else if (salario_bruto > 1500 && salario_bruto <= 2500){

        const IR = salario_bruto * 10/100

        const INSS = salario_bruto * 10/100

        const desconto_total = INSS + IR

        const salario_liquido = (salario_bruto - INSS) - IR


        return (`

        . Salário Bruto (${hora_trabalho} * ${valor_hora}) = R$ ${salario_bruto}

        . (-) IR (5%): R$ ${IR}

        . (-) INSS ( 10% ): R$ ${INSS}

        . FGTS (11 %): R$ ${FGTS}

        . Total de descontos: R$ ${desconto_total}

        . Salário Liquido : R$ ${salario_liquido}

        
        `)
    }
    else if (salario_bruto > 2500){

        const IR = salario_bruto * 20/100

        const INSS = salario_bruto * 10/100

        const desconto_total = INSS + IR

        const salario_liquido = (salario_bruto - INSS) - IR


        return (`

        . Salário Bruto (${hora_trabalho} * ${valor_hora}) = R$ ${salario_bruto}

        . (-) IR (5%): R$ ${IR}

        . (-) INSS ( 10% ): R$ ${INSS}

        . FGTS (11 %): R$ ${FGTS}

        . Total de descontos: R$ ${desconto_total}

        . Salário Liquido : R$ ${salario_liquido}

        
        `)
    }

}

main()