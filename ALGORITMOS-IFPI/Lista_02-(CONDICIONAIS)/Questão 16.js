// 16. Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior ou igual a 7,0. 
// Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média final. 
// Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve escreva “Reprovado”.

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

    if (media >= 7){

        return "APROVADO"
    } 

    else if ( media < 7){

        console.log ("VC ESTÁ DE PROVA FINAL")

    }
        
    const exame = get_number("Qual a nota da PROVA FINAL: ")

    const media_final = (exame + media / 2)

    if (media_final >= 5 ){

    return (`VC FOI APROVADO NA PROVA FINAL COM MÉDIA ${media_final}`)
    }
    else {

        return "REPROVADO!!"
    }

}

main()