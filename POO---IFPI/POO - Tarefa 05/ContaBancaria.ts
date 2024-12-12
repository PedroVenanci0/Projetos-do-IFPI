class Cliente{
    id: number
    nome: string
    cpf: string
    dataNascimento: Date
    contas = []

    constructor(id:number, nome:string, cpf:string,dataNascimento:Date){
        this.id = id
        this.nome = nome
        this.cpf = cpf
        this.dataNascimento = dataNascimento
    }
}

class Conta {
    numero: string;
    saldo: number;
    id: number;
    cliente: Cliente;

    constructor(numero: string, saldo: number) {
        this.numero = numero;
        this.saldo = saldo;
    }

    sacar(valor: number): void {
        this.saldo = this.saldo - valor;
    }

    depositar(valor: number): void {
        this.saldo = this.saldo + valor;
    }

    consultarSaldo(): number {
        return this.saldo
    }

    transferir(contaDestino: Conta, valor: number): void {
        // this.saldo = this.saldo - valor;
        // contaDestino.saldo = contaDestino.saldo + valor;

        this.sacar(valor);
        contaDestino.depositar(valor);
    }
}

/*
let contas: Conta[] = [];

let conta1 = new Conta('111-1',100);
let conta2 = new Conta('222-2',200);
contas[0] = conta1;
contas.push(conta2);

console.log(contas);
*/

class Banco {
    contas: Conta[];
    cliente: Cliente[];

    constructor() {
        this.contas = [];
    }

    inserirCliente(cliente: Cliente): void{
    }

    consultarCliente(cpf: string): Cliente{
    }

    associarContaCliente(numeroConta: string, cpfCliente: string): void{
    }

    listarContasCliente(cpf: string): Conta[]{
    }

    totalizarSaldoCliente(cpf: string): number{
    }

    inserirCliente(cliente: Cliente): void


    inserir(conta: Conta) {
        this.contas.push(conta);
    }

    consultar(numero: string): Conta {
        let contaProcurada!: Conta;

        for (let conta of this.contas) {
            if (conta.numero == numero) {
                contaProcurada = conta;
                break;
            }
        }


        return contaProcurada;
    }
}

let banco: Banco = new Banco();

banco.inserir(new Conta('111-1', 100));
banco.inserir(new Conta('222-2', 200));

console.log(banco.consultar('111-1'));
console.log(banco.consultar('333-3'));