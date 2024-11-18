var Conta_ = /** @class */ (function () {
    function Conta_(numero, saldo) {
        this.numero = numero;
        this.saldo = saldo;
    }
    Conta_.prototype.sacar = function (valor) {
        if (valor <= this.saldo) {
            this.saldo -= valor;
            return true;
        }
        return false;
    };
    Conta_.prototype.transferir = function (contaDestino, valor) {
        if (this.sacar(valor)) {
            contaDestino.saldo += valor;
            return true;
        }
        return false;
    };
    Conta_.prototype.consultarSaldo = function () {
        return this.saldo;
    };
    return Conta_;
}());
var conta01 = new Conta("1", 100);
var conta02 = new Conta("2", 50);
console.log(conta01.sacar(30));
console.log(conta01.sacar(80));
console.log(conta01.transferir(conta02, 50));
console.log(conta01.transferir(conta02, 200));
console.log(conta01.consultarSaldo());
console.log(conta02.consultarSaldo());
