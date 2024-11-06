/** 4. Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
o "Aprovado", se a média alcançada for maior ou igual a sete;
o "Reprovado", se a média for menor do que sete;
o "Aprovado com Distinção", se a média for igual a dez. */

import { get_number } from "../Exportar/io_utils.js";

function main(){

    console.log (" #### SITUAÇÃO ESCOLAR #### ")

    // Entrada 

    const nota_01 = get_number("Informe a primeira nota: ")
    const nota_02 = get_number("Informe a segunda nota: ")

    // Processamento

    const notas = situacao_escolar(nota_01, nota_02)

    // Saida

    console.log (notas)


}

function situacao_escolar(n1, n2){

    const media = (n1 + n2) / 2

    if (media >= 7 && media < 10){

        return "APROVADO"
    } 

    else if ( media < 7){

        return ("REPROVADO")

    }

    else if (media === 10){

        return "Aprovado com Distinção"
    }
        
    

}

main()