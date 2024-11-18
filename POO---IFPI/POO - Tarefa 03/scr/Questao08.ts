const array_ = [1, 2, 3, 4, 5];

// Usando o map para dobrar os elementos
const dobrados = array_.map((numero) => numero * 2);
console.log("Elementos dobrados:", dobrados);  

const soma_ = dobrados.reduce((acumulador, numero) => acumulador + numero, 0);
console.log("Soma dos elementos dobrados:", soma_);  