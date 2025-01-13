"use strict";
class Veiculo {
    constructor(placa, ano) {
        this.placa = placa;
        this.ano = ano;
    }
}
class Carro extends Veiculo {
    constructor(placa, ano, modelo) {
        super(placa, ano); // Chama o construtor da classe base
        this.modelo = modelo;
    }
}
class CarroEletrico extends Carro {
    constructor(placa, ano, modelo, autonomiaBateria) {
        super(placa, ano, modelo); // Chama o construtor da classe Carro
        this.autonomiaBateria = autonomiaBateria;
    }
}
