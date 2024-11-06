// 25. Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. 
// O algoritmo deve escrever uma mensagem de permissão de acesso ou não.

import { get_number } from "../Exportar/io_utils.js";

console.log (" #### Validando senha #### ")

function main(){

    // Entrada 

    const numero_senha = get_number("Informe sua senha: ")

    // processamento

    const senha = Validando_senha(numero_senha)

    // Saida

    console.log (senha)

}
function Validando_senha(senha){

    if (senha === 1234){

        return ("GOOD, senha correta!!!")
    } else{

        return ("hooo bad, senha incorreta!!!")
    }
}
main()