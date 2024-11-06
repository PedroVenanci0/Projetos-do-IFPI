// 9. Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).

import { question } from "readline-sync";

console.log ('ordem inversa dos números apresentados')

// Entrada 

var primeiro = Number(question('Digite o primeiro número a ser usado: '))

var segundo = Number(question('Digite o segundo número a ser usado: '))


// Processamento

console.log (`Esses números na ordem que foram apresentados são (${primeiro}, ${segundo})`)

// Saida

 console.log (`Já a ordem inversa desses numeros é (${segundo}, ${primeiro})`)