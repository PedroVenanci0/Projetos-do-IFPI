"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Conta = void 0;
class Conta {
    constructor(numero, saldo, id_conta) {
        this.numero = numero;
        this.saldo = saldo;
        this.id_conta = id_conta;
        this.st_assosciada = false;
    }
    sacar(valor) {
        this.saldo = this.saldo - valor;
    }
    depositar(valor) {
        this.saldo = this.saldo + valor;
    }
    consultarSaldo() {
        return this.saldo;
    }
    transferir(contaDestino, valor) {
        // this.saldo = this.saldo - valor
        // contaDestino.saldo = contaDestino.saldo + valor
        this.sacar(valor);
        contaDestino.depositar(valor);
    }
}
exports.Conta = Conta;
