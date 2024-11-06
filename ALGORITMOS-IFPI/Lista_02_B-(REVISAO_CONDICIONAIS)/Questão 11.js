/**11. Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
número. Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplos:
o 326 = 3 centenas, 2 dezenas e 6 unidades
o 12 = 1 dezena e 2 unidades */

import { get_number } from "../Exportar/io_utils.js";

console.log ("#### IDENTIFICANDO AS CASAS DECIMAIS ####")

function main(){

    // Entrada

    const numero = get_number("Informe um número menor que 1000: ")

    // Processamento

    const decimais = casas_decimais(numero)

    // Saida 

    console.log (decimais)


}

function casas_decimais(numero){

    if (numero === 0 ){

        return(`O número ${numero} = Valor Inválido`)
    }

    else if (numero === 1){

        return (`O número 1 = 1 unidade`)
    }

    else if (numero < 10){

        return (`O número ${numero} = ${numero} unidades`)
    }
    else if (numero === 10){

        const desmembrando_dezenas = numero / 10

        return (`O número ${numero} = ${desmembrando_dezenas} dezena`)
    }

    else if (numero > 10 && numero < 100 && Math.trunc(numero / 10) === 1 && numero % 10 === 1){

        const desmembrando_dezenas = Math.trunc(numero / 10)

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_dezenas} dezena e ${desmembrando_unidades} unidade`)
    }


    else if (numero > 10 && numero < 100 && Math.trunc(numero / 10) === 1 && numero % 10 > 1){

        const desmembrando_dezenas = Math.trunc(numero / 10)

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_dezenas} dezena e ${desmembrando_unidades} unidades `)
    }

    else if (numero > 10 && numero < 100 && Math.trunc(numero / 10) >= 2 && numero % 10 <= 1){

        const desmembrando_dezenas = Math.trunc(numero / 10)

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_dezenas} dezenas e ${desmembrando_unidades} unidade `)
    }

    else if (numero > 10 && numero < 100 && Math.trunc(numero / 10) > 2 && numero % 10 > 1){

        const desmembrando_dezenas = Math.trunc(numero / 10)

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_dezenas} dezenas e ${desmembrando_unidades} unidades `)
    }
    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) === 1 && numero % 10 === 0 && (Math.trunc(numero / 10)) % 10 === 0){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centena`)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) > 1 && (Math.trunc(numero / 10)) % 10 === 1 && numero % 10 > 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centanas, ${desmembrando_dezenas} dezena e ${desmembrando_unidades} unidades `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) === 1 && (Math.trunc(numero / 10)) % 10 === 1 && numero % 10 === 0){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centana e ${desmembrando_dezenas} dezena `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) === 1 && (Math.trunc(numero / 10)) % 10 === 0 && numero % 10 === 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centana e ${desmembrando_unidades} unidade `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) === 1 && (Math.trunc(numero / 10)) % 10 === 1 && numero % 10 === 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centana, ${desmembrando_dezenas} dezena e ${desmembrando_unidades} unidade `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) === 1 && (Math.trunc(numero / 10)) % 10 > 1 && numero % 10 === 0){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centana e ${desmembrando_dezenas} dezenas `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) === 1 && (Math.trunc(numero / 10)) % 10 > 1 && numero % 10 === 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centana, ${desmembrando_dezenas} dezenas e ${desmembrando_unidades} unidade `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) === 1 && (Math.trunc(numero / 10)) % 10 === 1 && numero % 10 > 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centana, ${desmembrando_dezenas} dezena e ${desmembrando_unidades} unidades `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) === 1 && (Math.trunc(numero / 10)) % 10 > 1 && numero % 10 > 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centana, ${desmembrando_dezenas} dezenas e ${desmembrando_unidades} unidades `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) > 1 && (Math.trunc(numero / 10)) % 10 === 1 && numero % 10 > 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centanas, ${desmembrando_dezenas} dezena e ${desmembrando_unidades} unidade `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) > 1 && (Math.trunc(numero / 10)) % 10 > 1 && numero % 10 === 0 ){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centanas , ${desmembrando_dezenas} dezenas e ${desmembrando_unidades} unidade `)
    }
        
    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) === 1 && (Math.trunc(numero / 10)) % 10 === 0 & numero % 10 > 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centana e ${desmembrando_unidades} unidades `)
    }
    
    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) > 1 && (Math.trunc(numero / 10)) % 10 > 1 && numero % 10 === 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centanas, ${desmembrando_dezenas} dezenas e ${desmembrando_unidades} unidade `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) > 1 && (Math.trunc(numero / 10)) % 10 === 0 & numero % 10 === 0){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centanas `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) > 1 && (Math.trunc(numero / 10)) % 10 > 1 & numero % 10 === 0 ){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centanas e ${desmembrando_dezenas} dezenas `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) > 1 && (Math.trunc(numero / 10)) % 10 === 0 & numero % 10 > 1 ){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centanas e ${desmembrando_unidades} unidades `)
    }

    else if (numero >= 100 && numero <= 999 && Math.trunc(numero / 100) > 1 && (Math.trunc(numero / 10)) % 10 > 1 & numero % 10 > 1){

        const desmembrando_centena = Math.trunc(numero / 100)

        const desmembrando_dezenas = (Math.trunc(numero / 10)) % 10

        const desmembrando_unidades = numero % 10 

        return (`O número ${numero} = ${desmembrando_centena} centanas, ${desmembrando_dezenas} dezenas e ${desmembrando_unidades} unidades `)
    }

    else {

        return (`Valor INVÁLIDO`)
    }
}
main()