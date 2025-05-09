"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
// Importando a classe Calculadora do arquivo Questão_02
const Quest_o_02_1 = require("./Quest\u00E3o_02");
class CalculadoraCientifica extends Quest_o_02_1.Calculadora {
    exponenciar() {
        // Acessando os atributos através de métodos herdados ou usando propriedades protegidas
        const base = this.operando1;
        const expoente = this.operando2;
        return Math.pow(base, expoente);
    }
}
// Testando a CalculadoraCientifica
const calcCientifica = new CalculadoraCientifica(2, 3);
console.log(`Soma: ${calcCientifica.soma()}`); // Saída: Soma: 5
console.log(`Exponenciação: ${calcCientifica.exponenciar()}`); // Saída: Exponenciação: 8
