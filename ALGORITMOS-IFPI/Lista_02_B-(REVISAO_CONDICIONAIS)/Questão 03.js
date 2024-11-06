// 3. Leia uma letra e verifique se a letra digitada é vogal ou consoante.

import { question } from "readline-sync"

console.log (" #### vogal ou consoante #### ")

function main(){

    // Entrada

    const letra = question("Informe uma letra:  ").toUpperCase()


    // Processamento

    const vogal_ou_consoante = verificaque(letra)

    // Saida

    console.log (vogal_ou_consoante)



}

function verificaque(letra){

    if (letra === "A" || letra === "E" || letra === "I" || letra === "O" || letra === "U"){

        return "A letra é uma VOGAL"
        
    } else {

        return ("A letra é uma CONSOANTE")
    }


}
main()