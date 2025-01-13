class Veiculo {
    placa: string;
    ano: number;
  
    constructor(placa: string, ano: number) {
      this.placa = placa;
      this.ano = ano;
    }
  }
  
  class Carro extends Veiculo {
    modelo: string;
  
    constructor(placa: string, ano: number, modelo: string) {
      super(placa, ano); // Chama o construtor da classe base
      this.modelo = modelo;
    }
  }
  
  class CarroEletrico extends Carro {
    autonomiaBateria: number;
  
    constructor(placa: string, ano: number, modelo: string, autonomiaBateria: number) {
      super(placa, ano, modelo); // Chama o construtor da classe Carro
      this.autonomiaBateria = autonomiaBateria;
    }
  }
  