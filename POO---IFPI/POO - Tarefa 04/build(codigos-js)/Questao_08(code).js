var Conta = /** @class */ (function () {
    function Conta(numero, saldo) {
        this.numero = numero;
        this.saldo = saldo;
    }
    Conta.prototype.sacar = function (valor) {
        if (valor <= this.saldo) {
            this.saldo -= valor;
            return true;
        }
        return false;
    };
    Conta.prototype.transferir = function (contaDestino, valor) {
        if (this.sacar(valor)) {
            contaDestino.saldo += valor;
            return true;
        }
        return false;
    };
    Conta.prototype.consultarSaldo = function () {
        return this.saldo;
    };
    return Conta;
}());
var conta1 = new Conta("1", 100);
var conta2 = new Conta("2", 50);
console.log(conta1.sacar(30));
console.log(conta1.sacar(80));
console.log(conta1.transferir(conta2, 50));
console.log(conta1.transferir(conta2, 200));
console.log(conta1.consultarSaldo());
console.log(conta2.consultarSaldo());
