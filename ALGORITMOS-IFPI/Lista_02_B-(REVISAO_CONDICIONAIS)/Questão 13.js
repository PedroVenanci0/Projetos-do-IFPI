/**13. Faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a) "Telefonou para a vítima ?"
b) "Esteve no local do crime ?"
c) "Mora perto da vítima ?"
d) "Devia para a vítima ?"
e) "Já trabalhou com a vítima ?"
O algoritmo deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa
responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como
"Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". */

import { question } from "readline-sync";

console.log (" #### Seja um detetive #### ")

function main(){

    // Entrada 

    const telefonou = question(" Você Telefonou para a vítima ? (S OU N) ").toUpperCase()
    const esteve_no_local = question(" Você Esteve no local do crime ? (S OU N) ").toUpperCase()
    const morava = question(" Você Mora perto da vítima ? (S OU N) ").toUpperCase()
    const devedor = question(" Devia para a vítima ? (S OU N) ").toUpperCase()
    const trabalhou = question(" Já trabalhou com a vítima ? (S OU N) ").toUpperCase()

    // Processamento 

    const O_detetive_esta_pensando = Se_vc_eh_o_Assassino(telefonou, esteve_no_local, morava, devedor, trabalhou)

    // Saida 

    console.log (O_detetive_esta_pensando)


}

function Se_vc_eh_o_Assassino(telefonou, esteve_no_local, morava, devedor, trabalhou){

    let provas = 0


    if (telefonou === "S"){
        provas += 1
    }
    if (esteve_no_local === "S"){
        provas += 1
    }
    if (morava === "S"){
        provas += 1
    }
    if (devedor === "S"){
        provas += 1
    }
    if (trabalhou === "S"){
        provas += 1
    }



    if (provas === 0){
        console.log ("Inocente")
    }

    else if (provas === 1){
        console.log ("Inocente")
    }
    
    else if (provas === 2){
        console.log ("Suspeito")
    }
    else if (provas === 3){
        console.log ("cúmplice")
    }
    else if (provas === 4){
        console.log ("cúmplice")
    }
    else if (provas === 5){
        console.log ("Assassino")
    }
}

main()