
  class Hotel { // Definição de uma classe chamada "Hotel"
    quantReservas: number; // Propriedade da classe do tipo number

    constructor(quantReservas: number = 0) { // Construtor que inicializa a propriedade da classe, com valor padrão 0
        this.quantReservas = quantReservas; // Atribuição do valor passado como parâmetro à propriedade da classe
    }

    adicionarReserva(): void { // Método que não retorna valor, mas incrementa a propriedade "quantReservas"
        this.quantReservas++;
    }
}

let hotel: Hotel = new Hotel(2); // Instancia um novo objeto da classe "Hotel" com o valor inicial 2 para "quantReservas"
console.log(hotel.quantReservas); // Exibe o valor atual da propriedade "quantReservas" no console
