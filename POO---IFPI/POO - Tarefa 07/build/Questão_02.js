"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Calculadora = void 0;
// Exportando a classe Calculadora para ser usada em outros arquivos
class Calculadora {
    constructor(operando1, operando2) {
        this.operando1 = operando1;
        this.operando2 = operando2;
    }
    soma() {
        return this.operando1 + this.operando2;
    }
}
exports.Calculadora = Calculadora;
// Testando a classe Calculadora
const calc = new Calculadora(10, 20);
console.log(`Soma: ${calc.soma()}`); // Saída: Soma: 30
