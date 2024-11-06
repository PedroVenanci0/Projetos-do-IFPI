// 22. Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras:hora e minuto). 
// Calcule e escreva a duração do jogo (horas e minutos), 
// sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia seguinte.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Quando começou e quando terminou o jogo #### ")

function main(){

    // Entrada

    const horas_inicio = get_number("Informe as horas de quando se iniciou o jogo: ")
    const minutos_inicio = get_number("Informe os minutos de quando se iniciou o jogo: ")
    const horas_termino = get_number("Informe as horas de quando se terminou o jogo: ")
    const minutos_termino = get_number("Informe os minutos de quando se terminou o jogo: ")

    // Processamento

    const duração = duracao_do_jogo(horas_inicio, minutos_inicio, horas_termino, minutos_termino)

 

    // Saida

    console.log (duração)



}

function duracao_do_jogo(horas_inicio, minutos_inicio, horas_termino, minutos_termino){

    if (horas_inicio > horas_termino){

        const horas_dia_seguinte = (Math.abs(horas_inicio - 24) + horas_termino) 

        const minuto_total_o = Math.abs(minutos_termino - minutos_inicio) 

        return (`A duração do jogo foi de ${horas_dia_seguinte} horas e ${minuto_total_o} minutos`)
    }
    
    const hora_total = Math.abs(horas_termino - horas_inicio)

    const minuto_total = Math.abs(minutos_termino - minutos_inicio) 

    return (`A duração do jogo foi de ${hora_total} horas e ${minuto_total} minutos`)

    
}

main()



