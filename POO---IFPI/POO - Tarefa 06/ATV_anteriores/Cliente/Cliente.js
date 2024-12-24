"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Cliente = void 0;
class Cliente {
    getNome() {
        return this.nome;
    }
    getCpf() {
        return this.cpf;
    }
    idCliente() {
        return this.id_cliente;
    }
    getContas() {
        return this.contas;
    }
    setContas(val) {
        return this.contas = val;
    }
    constructor(id_cliente, nome, cpf) {
        this.nome = nome;
        this.id_cliente = id_cliente;
        this.cpf = cpf;
        this.contas = [];
    }
}
exports.Cliente = Cliente;
