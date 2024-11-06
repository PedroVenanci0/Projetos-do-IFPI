// 17. Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
// escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
// são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
// divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
// escreva o quadrado dos números lidos.

import { question } from "readline-sync";

console.log (" #### Se for verdade, faça isso #### ")

function main(){

    // Entrada

    const num_1 = Number(question("Informe o primeiro numero: "))
    const num_2 = Number(question("Informe o segundo numero: "))

    // Processamento

     const Significado_do_resto = calculando_resto(num_1, num_2)

    // Saida

    console.log (Significado_do_resto)


}
function calculando_resto(n1, n2){

    if ( n1 % n2 === 1){

        return (soma_do_resto(n1, n2))
    }
    else if (n1 % n2 === 2){

        return (eh_par(n1,n2))
    }
    else if (n1 % n2 === 3){

        return (multiplicando_soma(n1, n2))
    }
    else if (n1 % n2 === 4 && n2 !== 0){

        return (divisao_soma(n1, n2))
    }
    else {
        return (quadrado(n1, n2))
    }
} 

function eh_par(n1, n2){

    if (n1 % 2 === 0 && n2 % 2 === 0){

    return (`Os dois números são pares`)

    } else if (n1 % 2 !== 0 && n2 % 2 !== 0){

    return (`Os dois números são Impares`)

    } else if (n1 % 2 === 0 && n2 % 2 !== 0){

    return ("O Primeiro número é PAR e o segundo é IMPAR")

    } else if (n1 % 2 !== 0 && n2 % 2 === 0){

    return ("O Primeiro número é IMPAR e o segundo é PAR")

    }

}

function quadrado(n1, n2){

    const calculando_n1 = n1**2
    const calculando_n2 = n2**2

    return (`O quadrado do primeiro número é ${calculando_n1}, já o quadrado do segundo é ${calculando_n2}`)

}

function soma_do_resto(n1, n2){

    const calculando_somatorio = (n1 + n2 + 1)

    return (`A soma dessas variaveis mais o resto da divisão é ${calculando_somatorio} `)
}

function multiplicando_soma(n1, n2){

    const calculando_multiplicaçao = (n1 + n2) * n1

    return (`A multiplicação da soma dos valores lidos pelo primeiro número é ${calculando_multiplicaçao}`)
}

function divisao_soma(n1, n2){

    const calculando_divisao = ((n1 + n2) / n2).toFixed(2)

    return (`A divisão da soma dos números lidos pelo segundo número é ${calculando_divisao}`)
}
main()