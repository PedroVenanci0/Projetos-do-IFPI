class Radio { // Definição de uma classe chamada "Radio"
  volume: number; // Propriedade da classe do tipo number

  constructor(volume: number = 0) { // Construtor que inicializa a propriedade "volume" com valor padrão 0
      this.volume = volume; // Atribui o valor passado ao parâmetro "volume" à propriedade da classe
  }
}

let r: Radio = new Radio(); // Criação de um novo objeto da classe "Radio", com o valor padrão de volume sendo 0
r.volume = 10; // Atualização do valor da propriedade "volume" do objeto "r" para 10
console.log(r.volume); // Exibe no console o valor atual da propriedade "volume" do objeto "r"
