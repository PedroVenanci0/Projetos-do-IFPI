/**7. As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe
contrataram para desenvolver o programa que calculará os reajustes. Escreva um algoritmo que leia o
salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
o salários até R$ 280,00 (incluindo) : aumento de 20%
o salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
o salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
o salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
· o salário antes do reajuste;
· o percentual de aumento aplicado;
· o valor do aumento;
· o novo salário, após o aumento. */

import { get_number } from "../Exportar/io_utils.js";

console.log (" **** Salarios Organização Tabajara **** ")

function main(){

    // Entrada 

    const salario = get_number("Informe seu sálario: ")

    // Processamento 

    const reajuste_salarial = aumento_salarial(salario)



    // Saida

    console.log (reajuste_salarial)



}

function aumento_salarial(salario){

    if (salario <= 280){

        const salario_20 = (salario * 20/100) + salario

        const salario_20_diferença = salario * 20/100

    

        return (` 

        -------------------------------------------------

        . o salário antes do reajuste: ${salario}

        · o percentual de aumento aplicado: 20%

        . o valor do aumento: ${salario_20_diferença}

        . o novo salário, após o aumento: ${salario_20}

        -------------------------------------------------
        
        `)
        
    }

    else if (salario > 280 && salario <= 700){


        
        const salario_15 = (salario * 15/100) + salario

        const salario_15_diferença = (salario * 15/100) 

    

        return (` 

        -------------------------------------------------

        . o salário antes do reajuste: ${salario}

        · o percentual de aumento aplicado: 15%

        . o valor do aumento: ${salario_15_diferença}

        . o novo salário, após o aumento: ${salario_15}

        -------------------------------------------------

         
        
        `)

    }

    else if (salario > 700 && salario <= 1500){

        
        const salario_10 = (salario * 10/100) + salario

        const salario_10_diferença = (salario * 10/100) 

    

        return (` 

        -------------------------------------------------

        . o salário antes do reajuste: ${salario}

        · o percentual de aumento aplicado: 10%

        . o valor do aumento: ${salario_10_diferença}

        . o novo salário, após o aumento: ${salario_10}

        -------------------------------------------------
        
        `)
    }

    else if (salario > 1500){

        
            const salario_5 = (salario * 5/100) + salario
     
            const salario_5_diferença = (salario * 5/100) 
    
        
    
        return (` 

        -------------------------------------------------
    
        . o salário antes do reajuste: ${salario}
    
        · o percentual de aumento aplicado: 5%
    
        . o valor do aumento: ${salario_5_diferença}
    
        . o novo salário, após o aumento: ${salario_5}
    
        -------------------------------------------------
        
        `)
        
    }

}

main()