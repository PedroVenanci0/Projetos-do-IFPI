// Leia (um) número entre 0 e 100, verifique e escreva se o número é ou não primo 

import { question } from "readline-sync";

function main(){

    const numero = Number(question("Informe um numero entre 0 e 100: ")) 
    const identificao_num = identificacao(numero)
    console.log(identificao_num)

}

function identificacao(numero){

    if (numero === 1 || numero === 2 || numero === 3 || numero === 5) {

        return (" O numero é primo ")
    }
    
    if (numero / 2 || numero / 3 || numero / 5){

            return ("O número não é primo")
        }

    if (numero === 0){

        return ("O número não é primo")

    }

        else (numero / numero === 1 && numero / 1 === numero )

        return ("O número é primo")







    }




main()