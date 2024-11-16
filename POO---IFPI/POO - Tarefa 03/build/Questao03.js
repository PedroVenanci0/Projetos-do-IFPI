"use strict";
class ListaNumeros {
    constructor(lista) {
        this.lista = lista;
    }
    organizandoLista() {
        let organizandoNumeros = "";
        this.lista.forEach((value, index) => {
            organizandoNumeros += value.toString();
            if (index < this.lista.length - 1) {
                organizandoNumeros += " - ";
            }
        });
        return organizandoNumeros;
    }
}
const numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
const lista = new ListaNumeros(numeros);
console.log(lista.organizandoLista());
