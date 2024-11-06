// 14. Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

import { question } from "readline-sync";

console.log (" #### números maiores que a média #### ")

function main(){

    console.log ("Explane 5 números inteiros")

    // Entrada 

    const num_1 = Number(question("Informe o primeiro número: "))
    const num_2 = Number(question("Informe o segundo número: "))
    const num_3 = Number(question("Informe o terceiro número: "))
    const num_4 = Number(question("Informe o quarto número: "))
    const num_5 = Number(question("Informe o quinto número: "))

    // processamento

    const Maior_que_a_media = calculando_maior(num_1, num_2, num_3, num_4, num_5)

    // Saida

    console.log (Maior_que_a_media)

}


function calculando_maior(n1, n2, n3, n4, n5){

    const media = (n1 + n2 + n3 + n4 + n5) / 5

    if (n1 > media && n2 > media){

        return (`os maiores numeros sao ${n1} e ${n2}`)
    }
    else if (n1 > media && n3 > media){

        return (`os maiores numeros sao ${n1} e ${n3}`)
    }
    else if (n1 > media && n4 > media){

        return (`os maiores numeros sao ${n1} e ${n4}`)
    }
    else if (n1 > media && n5 > media){

        return (`os maiores numeros sao ${n1} e ${n5}`)
    }
    else if (n2 > media && n3 > media){

        return (`os maiores numeros sao ${n2} e ${n3}`)
    }
    else if (n2 > media && n4 > media){

        return (`os maiores numeros sao ${n2} e ${n4}`)
    }
    else if (n2 > media && n5 > media){

        return (`os maiores numeros sao ${n2} e ${n5}`)
    }
    else if (n3 > media && n4 > media){

        return (`os maiores numeros sao ${n3} e ${n4}`)
    }
    else if (n3 > media && n5 > media){

        return (`os maiores numeros sao ${n3} e ${n5}`)
    }
    else if (n4 > media && n5 > media){

        return (`os maiores numeros sao ${n4} e ${n5}`)

    }

    else if (n1 > media && n2 < media && n3 < media && n4 < media && n5 < media){

        return (`O número ${n1} é maior que a média`)
    }
    else if (n2 > media && n1 < media && n3 < media && n4 < media && n5 < media){

        return (`O número ${n2} é maior que a média`)
    }
    else if (n3 > media && n2 < media && n1 < media && n4 < media && n5 < media){

        return (`O número ${n3} é maior que a média`)
    }
    else if (n4 > media && n2 < media && n3 < media && n1 < media && n5 < media){

        return (`O número ${n4} é maior que a média`)
    }
    else if (n5 > media && n2 < media && n3 < media && n4 < media && n1 < media){

        return (`O número ${n5} é maior que a média`)
    }

    else if (n1 > media && n2 > media && n3 > media){

        return (`os maiores numeros sao ${n1}, ${n2} e ${n3}`)
    }

    else if (n1 > media && n3 > media && n4 > media){

        return (`os maiores numeros sao ${n1}, ${n3} e ${n4}`)
    }

    else if (n1 > media && n3 > media && n5 > media){

        return (`os maiores numeros sao ${n1}, ${n3} e ${n5}`)
    }

    else if (n1 > media && n2 > media && n4 > media){

        return (`os maiores numeros sao ${n1}, ${n2} e ${n4}`)
    }

    else if (n1 > media && n2 > media && n5 > media){

        return (`os maiores numeros sao ${n1}, ${n2} e ${n5}`)
    }

    else if (n1 > media && n4 > media && n5 > media){

        return (`os maiores numeros sao ${n1}, ${n4} e ${n5}`)
    }

    else if (n2 > media && n3 > media && n4 > media){

        return (`os maiores numeros sao ${n2}, ${n3} e ${n4}`)
    }

    else if (n2 > media && n3 > media && n5 > media){

        return (`os maiores numeros sao ${n2}, ${n3} e ${n5}`)
    }

    else if (n2 > media && n4 > media && n5 > media){

        return (`os maiores numeros sao ${n2}, ${n4} e ${n5}`)
    }

    else if (n3 > media && n4 > media && n5 > media){

        return (`os maiores numeros sao ${n3}, ${n4} e ${n5}`)
    }

    
}

main()