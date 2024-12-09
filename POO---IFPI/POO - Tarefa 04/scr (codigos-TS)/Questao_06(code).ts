
  class Saudacao {  // Definição de uma classe chamada "Saudacao"
    texto: string;  // Propriedade "texto" do tipo string
    destinatario: string; // Propriedade "destinatario" do tipo string

    constructor(texto: string, destinatario: string) { // Construtor que inicializa as propriedades "texto" e "destinatario"
        this.texto = texto; // Atribui o valor recebido no parâmetro "texto" à propriedade da classe
        this.destinatario = destinatario; // Atribui o valor recebido no parâmetro "destinatario" à propriedade da classe
    }

    obterSaudacao(): string { // Método que retorna uma saudação concatenando as propriedades "texto" e "destinatario"
        return `${this.texto}, ${this.destinatario}`; // Retorna a saudação no formato "texto, destinatario"
    }
}

const saudacao = new Saudacao("Bom dia", "João"); // Criação de um novo objeto da classe "Saudacao" com os argumentos "Bom dia" e "João"
console.log(saudacao.obterSaudacao()); // Chamada do método "obterSaudacao" para exibir a saudação no console
