"use strict";
const array = [1, 2, 3, 4, 5];
// Usando o map para dobrar os elementos
const dobrados = array.map((numero) => numero * 2);
console.log("Elementos dobrados:", dobrados);
const soma = dobrados.reduce((acumulador, numero) => acumulador + numero, 0);
console.log("Soma dos elementos dobrados:", soma);
