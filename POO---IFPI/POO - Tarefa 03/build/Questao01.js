"use strict";
class identificandoNumero {
    constructor(numero) {
        this.numero = numero;
    }
    verificarNumero() {
        if (this.numero % 2 == 0)
            return "Esse numero é par";
        else {
            return "Esse numero é impar";
        }
    }
}
const numeroObj = new identificandoNumero(22);
console.log(numeroObj.verificarNumero());
