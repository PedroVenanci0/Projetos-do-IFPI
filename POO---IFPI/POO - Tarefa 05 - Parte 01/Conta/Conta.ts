import { Cliente } from "../Cliente/Cliente"

export class Conta {
    numero: string
    saldo: number
    id_conta: number
    cliente: Cliente
    st_assosciada: boolean //esta associada

    constructor(numero: string, saldo: number, id_conta: number) {
        this.numero = numero
        this.saldo = saldo
        this.id_conta = id_conta
        this.st_assosciada = false
        
    }

    sacar(valor: number): void {
        this.saldo = this.saldo - valor
    }

    depositar(valor: number): void {
        this.saldo = this.saldo + valor
    }

    consultarSaldo(): number {
        return this.saldo
    }

    transferir(contaDestino: Conta, valor: number): void {
        // this.saldo = this.saldo - valor
        // contaDestino.saldo = contaDestino.saldo + valor

        this.sacar(valor)
        contaDestino.depositar(valor)
    }
}
