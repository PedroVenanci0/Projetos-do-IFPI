// 27. Determine a idade de uma pessoa, em anos, meses e dias, dadas a data (dia, mês e ano) do seu nascimento e a data (dia, mês e ano) atual.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Determinando idade #### ")

function main(){

    // ENTRADA

    const dia_nascimento = get_number("Informe o dia de seu nascimento:  ")
    const mes_nascimento = get_number("Informe o mês de seu nascimento: ")
    const ano_nascimento = get_number("Informe o ano de seu nascimento: ")

    const dia_atual = get_number("Informe o dia atual: ")
    const mes_atual = get_number("Informe o mês atual: ")
    const ano_atual = get_number("Informe o ano atual: ")

    // Processamento

    const idade = identificando_idade(dia_nascimento, mes_nascimento, ano_nascimento, dia_atual, mes_atual, ano_atual)

    // Saida

    console.log (idade)



}

function identificando_idade(dia_N, mes_N, ano_N, dia_A, mes_A, ano_A){

    const idade = ano_A - ano_N

    if (mes_A < mes_N || mes_A === mes_N && dia_A < dia_N){

      const ano = (idade - 1)

    const mes_real = Math.abs(Math.abs(mes_A - mes_N) - 12)

    const dia_real = Math.abs(dia_A - dia_N)

    return (`Sua idade corresponde a ${ano} anos, ${mes_real} meses e ${dia_real} dias`)

}
}
main()