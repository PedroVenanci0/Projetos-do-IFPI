// 2. Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido.

import { question } from "readline-sync"


console.log (" #### identificando sexo Masculino e Feminino #### ")

function main(){

    // Entrada

    console.log (" **** digite F para Femenino ou M para Masculino **** ")

    const letra = question("Informe a letra correspondente ao Sexo procurado: ").toUpperCase

    // Processamento 

    const masculino_ou_feminino = Identificando_sexo(letra)

    // Saida 

    console.log (masculino_ou_feminino)


}

function Identificando_sexo(letra){

    if (letra === "F" ){

        return "F - Feminino"

    }

    else if (letra === "M" ){

        return "M - Masculino"
    }

    else {

        return ("Sexo inválido")
    }
}
main()
