var Equipamento = /** @class */ (function () {
    function Equipamento() {
        this.ligado = false;
    }
    Equipamento.prototype.liga = function () {
        if (!this.ligado) {
            this.ligado = true;
            console.log("Equipamento ligado.");
        }
        else {
            console.log("O equipamento já está ligado.");
        }
    };
    Equipamento.prototype.desliga = function () {
        if (this.ligado) {
            this.ligado = false;
            console.log("Equipamento desligado.");
        }
        else {
            console.log("O equipamento já está desligado.");
        }
    };
    Equipamento.prototype.inverte = function () {
        this.ligado = !this.ligado;
        if (this.ligado) {
            console.log("Equipamento agora ligado.");
        }
        else {
            console.log("Equipamento agora desligado.");
        }
    };
    Equipamento.prototype.estaLigado = function () {
        return this.ligado;
    };
    return Equipamento;
}());
var meuEquipamento = new Equipamento();
meuEquipamento.liga();
meuEquipamento.liga();
meuEquipamento.desliga();
meuEquipamento.desliga();
meuEquipamento.inverte();
meuEquipamento.inverte();
console.log("Está ligado?", meuEquipamento.estaLigado());
