"use strict";
class Pessoa {
    constructor(nome, pronome = "Sr") {
        this.nome = nome;
        this.pronome = pronome;
    }
    verificandoNome() {
        return `${this.pronome}. ${this.nome}`;
    }
}
// Teste com o pronome fornecido
const objetoNome1 = new Pessoa("Sávia", "Sra");
console.log(objetoNome1.verificandoNome());
const objetoNome2 = new Pessoa("Pedro");
console.log(objetoNome2.verificandoNome());
