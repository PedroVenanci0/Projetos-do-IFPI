"use strict";
class Calculadora {
    constructor(operando1, operando2) {
        this.operando1 = operando1;
        this.operando2 = operando2;
    }
    somar() {
        return this.operando1 + this.operando2;
    }
    subtrair() {
        return this.operando1 - this.operando2;
    }
    multiplicar() {
        return this.operando1 * this.operando2;
    }
    dividir() {
        if (!this.operando2) {
            return ("Não é possível dividir por zero.");
        }
        return this.operando1 / this.operando2;
    }
}
const calc = new Calculadora(10, 0);
console.log("Soma: " + calc.somar());
console.log("Subtração: " + calc.subtrair());
console.log("Multiplicação: " + calc.multiplicar());
console.log("Divisão: " + calc.dividir());
