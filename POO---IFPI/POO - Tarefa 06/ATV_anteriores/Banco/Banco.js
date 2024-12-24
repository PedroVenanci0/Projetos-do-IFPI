"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.Banco = void 0;
class Banco {
    constructor() {
        this.data = {
            totDepositado: 0,
            saldoMedioContas: 0
        };
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
    }
    inserirCliente(cliente) {
        if (this.clienteJaExiste(cliente.idCliente(), cliente.getCpf())) {
            console.error(`Já existe uma conta com o id ${cliente.idCliente()} ou um cpf ${cliente.getCpf()} cadastrado. Não é possível adicionar.`);
        }
        else {
            this.clientes.push(cliente);
            console.log(`Cliente ${cliente.getNome()} cadastrado com sucesso`);
        }
    }
    clienteJaExiste(id, cpf) {
        return this.clientes.some(cli => cli.getCpf() === cpf || cli.idCliente() === id);
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
        const result = this.clientes.filter((key) => key.getCpf() === cpf);
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
        cliente.getContas().push(conta);
        this.mudarStatusConta(conta);
        console.log(`Conta ${numeroConta} associada com sucesso ao cliente ${cliente.getNome()}.`);
    }
    mudarStatusConta(conta) {
        conta.st_assosciada = true;
    }
    listarContasDeUmCliente(cpfCliente) {
        const cliente = this.consultaPorCpf(cpfCliente);
        return cliente === null || cliente === void 0 ? void 0 : cliente.getContas();
    }
    totalizadorSaldoCliente(cpf) {
        const contasDeCliente = this.listarContasDeUmCliente(cpf);
        let totalizador = 0;
        contasDeCliente === null || contasDeCliente === void 0 ? void 0 : contasDeCliente.forEach(element => {
            totalizador += element.saldo;
        });
        return totalizador;
    }
    removerContaVinculada(cpf, numeroConta) {
        const clientesIndex = this.retornarContaCliente(cpf, numeroConta);
        if (!clientesIndex)
            return;
        const [cliente, contaIndex] = clientesIndex;
        cliente.getContas().splice(contaIndex, 1);
        console.log(`Conta ${numeroConta} removida com sucesso do cliente ${cliente.getNome()}.`);
    }
    sacar(cpf, numeroConta, valSacado, ie_trans) {
        const clientesIndex = this.retornarContaCliente(cpf, numeroConta);
        if (!clientesIndex)
            return false;
        const [cliente, contaIndex] = clientesIndex;
        let saldoCliente = cliente.getContas()[contaIndex].saldo;
        if (saldoCliente < valSacado) {
            console.log("Você não tem saldo o suficiente");
            return false;
        }
        cliente.getContas()[contaIndex].saldo -= valSacado;
        if (!ie_trans)
            console.log(`Valor de R$${valSacado} sacado com sucesso`);
        return true;
    }
    depositar(cpf, numeroConta, valDeposito, ie_trans) {
        const clientesIndex = this.retornarContaCliente(cpf, numeroConta);
        if (!clientesIndex)
            return false;
        const [cliente, contaIndex] = clientesIndex;
        cliente.getContas()[contaIndex].saldo += valDeposito;
        this.totDepositado(valDeposito);
        if (!ie_trans)
            console.log("Deposito realizado com sucesso!");
        return true;
    }
    trasnferir(cpfRemetente, numeroContaRemetente, cpfDestino, numeroContaDestino, valTransferido) {
        const clientesIndexRemetente = this.retornarContaCliente(cpfRemetente, numeroContaRemetente);
        const clientesIndexDestino = this.retornarContaCliente(cpfDestino, numeroContaDestino);
        if (!clientesIndexRemetente || !clientesIndexDestino)
            return;
        if (this.sacar(cpfRemetente, numeroContaRemetente, valTransferido, true)) {
            this.depositar(cpfDestino, numeroContaDestino, valTransferido, true);
            console.log("Valor Transferido com Sucesso");
        }
    }
    retornarContaCliente(cpf, numeroConta) {
        const cliente = this.consultaPorCpf(cpf);
        if (!cliente) {
            console.log('Cliente não encontrado!');
            return;
        }
        const contaIndex = cliente.getContas().findIndex(conta => conta.numero === numeroConta);
        if (contaIndex === -1) {
            console.log('Conta não encontrada!');
            return;
        }
        return [cliente, contaIndex];
    }
    transferirParaVarios(cpfRemetente, numeroContaRemetente, contasDestinatarios, valTransferido) {
        // Encontra a conta do remetente
        const clientesIndexRemetente = this.retornarContaCliente(cpfRemetente, numeroContaRemetente);
        if (!clientesIndexRemetente) {
            console.log('Remetente não encontrado ou conta inválida.');
            return;
        }
        const [clienteRemetente, contaIndexRemetente] = clientesIndexRemetente;
        // Verifica se o saldo do remetente é suficiente para realizar todas as transferências
        const saldoRemetente = clienteRemetente.getContas()[contaIndexRemetente].saldo;
        if (saldoRemetente < valTransferido * contasDestinatarios.length) {
            console.log('Saldo insuficiente para transferir para todas as contas.');
            return;
        }
        // Itera sobre as contas destinatárias e realiza a transferência
        contasDestinatarios.forEach(({ cpfDestino, numeroContaDestino }) => {
            const clientesIndexDestino = this.retornarContaCliente(cpfDestino, numeroContaDestino);
            if (!clientesIndexDestino) {
                console.log(`Conta destino não encontrada para CPF: ${cpfDestino} e número de conta: ${numeroContaDestino}`);
                return;
            }
            const [clienteDestino, contaIndexDestino] = clientesIndexDestino;
            // Realiza o saque da conta remetente e o depósito na conta destino
            if (this.sacar(cpfRemetente, numeroContaRemetente, valTransferido)) {
                this.depositar(cpfDestino, numeroContaDestino, valTransferido);
                console.log(`Transferência de R$${valTransferido} realizada para a conta de ${cpfDestino}`);
            }
            else {
                console.log(`Falha ao realizar a transferência para a conta de ${cpfDestino}`);
            }
        });
    }
    excluirCliente(cpf) {
        const clienteIndex = this.clientes.findIndex(cliente => cliente.getCpf() === cpf);
        if (clienteIndex === -1) {
            console.log(`Cliente não encontrado.`);
            return;
        }
        const cliente = this.clientes[clienteIndex];
        cliente.getContas().forEach(conta => {
            conta.st_assosciada = false;
        });
        this.clientes.splice(clienteIndex, 1);
        console.log(`Cliente ${cliente.getNome()} excluído com sucesso.`);
    }
    excluirConta(numeroConta) {
        const conta = this.consultar(numeroConta);
        if (!conta) {
            console.log(`Conta ${numeroConta} não encontrada.`);
            return;
        }
        const cliente = this.clientes.find(cliente => cliente.getContas().includes(conta));
        if (cliente) {
            cliente.setContas(cliente.getContas().filter(conta => conta.numero !== numeroConta));
            if (cliente.getContas().length === 0) {
                this.excluirCliente(cliente.getCpf());
            }
        }
        const index = this.contas.findIndex(c => c.numero === numeroConta);
        this.contas.splice(index, 1);
        console.log(`Conta ${numeroConta} excluída com sucesso.`);
    }
    mudarTitularidadeConta(numeroConta, novoCpfCliente) {
        const conta = this.consultar(numeroConta);
        const novoCliente = this.consultaPorCpf(novoCpfCliente);
        if (!conta || !novoCliente) {
            console.log("Conta ou cliente não encontrado.");
            return;
        }
        if (conta.st_assosciada) {
            const clienteAtual = this.clientes.find(cliente => cliente.getContas().includes(conta));
            clienteAtual === null || clienteAtual === void 0 ? void 0 : clienteAtual.getContas().splice(clienteAtual.getContas().indexOf(conta), 1);
        }
        novoCliente.getContas().push(conta);
        conta.st_assosciada = true;
        console.log(`Titularidade da conta ${numeroConta} alterada para o cliente ${novoCliente.getNome()}.`);
    }
    listarContasSemCliente() {
        return this.contas.filter(conta => !conta.st_assosciada);
    }
    associarContaSemCliente(numeroConta, cpfCliente) {
        const conta = this.consultar(numeroConta);
        const cliente = this.consultaPorCpf(cpfCliente);
        if (!conta || !cliente) {
            console.log("Conta ou cliente não encontrado.");
            return;
        }
        if (conta.st_assosciada) {
            console.log("Essa conta já está associada a um cliente.");
            return;
        }
        cliente.getContas().push(conta);
        conta.st_assosciada = true;
        console.log(`Conta ${numeroConta} associada com sucesso ao cliente ${cliente.getNome()}.`);
    }
    totalDeContas() {
        this.contas = this.contas.filter((value, index, self) => index === self.findIndex((t) => t.id_conta === value.id_conta));
        return this.contas.length;
    }
    totDepositado(valDeposito) {
        this.data.totDepositado += valDeposito;
    }
    saldoMedioContas() {
        this.contas.forEach(conta => { this.data.saldoMedioContas += conta.saldo; });
        this.data.saldoMedioContas = this.data.saldoMedioContas / this.totalDeContas();
        return this.data.saldoMedioContas;
    }
}
exports.Banco = Banco;
