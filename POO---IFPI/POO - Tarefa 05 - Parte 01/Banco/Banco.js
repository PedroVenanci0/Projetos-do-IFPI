"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Banco = void 0;
class Banco {
    constructor() {
        this.contas = [];
        this.clientes = [];
    }
    inserirConta(conta) {
        if (this.contaJaExiste(conta.id_conta, conta.numero)) {
            console.error(`Já existe uma conta com o id ${conta.id_conta} ou um numero de conta ${conta.numero} cadastrado. Não é possível adicionar.`);
        }
        else {
            this.contas.push(conta);
            console.log(`Conta ${conta.numero} cadastrado com sucesso`);
        }
        this.contas.push(conta);
    }
    inserirCliente(cliente) {
        if (this.clienteJaExiste(cliente.id_cliente, cliente.cpf)) {
            console.error(`Já existe uma conta com o id ${cliente.id_cliente} ou um cpf ${cliente.cpf} cadastrado. Não é possível adicionar.`);
        }
        else {
            this.clientes.push(cliente);
            console.log(`Cliente ${cliente.nome} cadastrado com sucesso`);
        }
    }
    clienteJaExiste(id, cpf) {
        return this.clientes.some(cli => cli.cpf === cpf || cli.id_cliente === id);
    }
    contaJaExiste(id, numeroConta) {
        return this.contas.some(conta => conta.numero === numeroConta || conta.id_conta === id);
    }
    consultar(numero) {
        const contaProcurada = this.contas.filter(conta => conta.numero === numero);
        if (!contaProcurada) {
            console.error(`Conta com número ${numero} não encontrada.`);
            return null;
        }
        return contaProcurada[0];
    }
    consultaPorCpf(cpf) {
        const result = this.clientes.filter((key) => key.cpf === cpf);
        if (!result) {
            console.error(`Cliente com CPF ${cpf} não encontrado.`);
            return null;
        }
        return result[0];
    }
    associarContaCliente(numeroConta, cpfCliente) {
        const cliente = this.consultaPorCpf(cpfCliente);
        const conta = this.consultar(numeroConta);
        if (!cliente || !conta)
            return;
        if (conta.st_assosciada) {
            console.error(`A conta ${conta.numero} já está associada a outro cliente.`);
            return;
        }
        cliente.contas.push(conta);
        this.mudarStatusConta(conta);
        console.log(`Conta ${numeroConta} associada com sucesso ao cliente ${cliente.nome}.`);
    }
    mudarStatusConta(conta) {
        conta.st_assosciada = true;
    }
    listarContasDeUmCliente(cpfCliente) {
        const cliente = this.consultaPorCpf(cpfCliente);
        return cliente === null || cliente === void 0 ? void 0 : cliente.contas;
    }
    totalizadorSaldoCliente(cpf) {
        const contasDeCliente = this.listarContasDeUmCliente(cpf);
        let totalizador = 0;
        contasDeCliente === null || contasDeCliente === void 0 ? void 0 : contasDeCliente.forEach(element => {
            totalizador += element.saldo;
        });
        return totalizador;
    }
}
exports.Banco = Banco;
