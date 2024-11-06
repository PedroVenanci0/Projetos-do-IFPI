// 23. Leia um valor em kg (quilograma), calcule e escreva o equivalente em g (grama).

import { question } from "readline-sync"

console.log ('conversor de kg (quilograma) para g (grama)')

// Entrada 

var kg = Number(question('Informe o valor em kg (quilograma): '))

// Processamento 

const g = kg * 1000 

// Saida 

console.log (`O valor em g (gramas) corresponde a ${g} `)