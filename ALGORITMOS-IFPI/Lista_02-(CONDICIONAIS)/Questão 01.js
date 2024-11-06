// 1. Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.

import { question } from "readline-sync"


function main(){

 // Entrada

const numero_01 = get_number(" Informe o primeiro número:  ")
const numero_02 = get_number(" Informe o segundo número:   ")
const numero_03 = get_number(" Informe o terceiro número:  ")

print (`${iguais(numero_01,numero_02,numero_03)}`)



}

function iguais (numero_01, numero_02, numero_03){

    if (numero_01 === numero_02 && numero_01 === numero_03 && numero_02 === numero_03)

    return `Existem 3 números iguais`

    else if (numero_01 === numero_02 || numero_02 === numero_03 || numero_03 === numero_01)

    return `Existem 2 numeros iguais`

    else if (numero_01 !== numero_02 !== numero_03)

    return `NÃO HÀ NÚMEROS IGUAIS`




}

function get_number(mensagem){
    return Number(question(mensagem))

  }

  function print(mensagem){
    console.log(mensagem)

  }

main()
