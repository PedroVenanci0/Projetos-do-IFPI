class Jogador { // Classe Jogador representa um jogador com atributos e métodos para interagir em combate
    private forca: number; // Atributo privado que representa a força do jogador
    private nivel: number; // Atributo privado que representa o nível do jogador
    private pontos: number; // Atributo privado que representa os pontos de vida do jogador

    constructor(forca: number, nivel: number, pontos: number) { // Construtor para inicializar os atributos da classe
        this.forca = forca;
        this.nivel = nivel;
        this.pontos = pontos;
    }

    calcularAtaque(): number { // Método para calcular o dano causado pelo jogador ao atacar
        return this.forca * this.nivel; // O dano é o produto da força pelo nível
    }

    atacar(jogadorAtacado: Jogador): void { // Método que permite ao jogador atacar outro jogador
        if (jogadorAtacado.estaVivo()) { // Verifica se o jogador atacado ainda está vivo
            const dano = this.calcularAtaque(); // Calcula o dano do ataque
            jogadorAtacado.receberDano(dano); // Aplica o dano ao jogador atacado
            console.log(`${this.toString()} atacou ${jogadorAtacado.toString()} causando ${dano} de dano.`); // Exibe mensagem do ataque
        } else {
            console.log(`${jogadorAtacado.toString()} não pode ser atacado, pois já está morto.`); // Caso o jogador já esteja morto
        }
    }

    estaVivo(): boolean { // Método que verifica se o jogador ainda está vivo
        return this.pontos > 0; // Retorna true se os pontos de vida forem maiores que zero
    }

    private receberDano(dano: number): void { // Método privado que reduz os pontos de vida do jogador
        this.pontos -= dano; // Subtrai o dano dos pontos de vida
    }

    toString(): string { // Método que retorna uma descrição textual do estado atual do jogador
        return `Jogador [Força: ${this.forca}, Nível: ${this.nivel}, Pontos: ${this.pontos}]`;
    }
}

let jogador1 = new Jogador(10, 5, 100); // Jogador 1: força 10, nível 5, 100 pontos de vida
let jogador2 = new Jogador(8, 4, 100);  // Jogador 2: força 8, nível 4, 100 pontos de vida


jogador1.atacar(jogador2);   // Jogador 1 ataca o Jogador 2


jogador2.atacar(jogador1);  // Jogador 2 ataca o Jogador 1 

// Exibe os estados dos jogadores após os ataques
console.log(jogador1.toString());  
console.log(jogador2.toString());  


if (jogador1.estaVivo()) { // Verifica se o Jogador 1 ainda está vivo
    console.log("Jogador 1 está vivo!");
} else {
    console.log("Jogador 1 morreu.");
}

 
if (jogador2.estaVivo()) { // Verifica se o Jogador 2 ainda está vivo
    console.log("Jogador 2 está vivo!");
} else {
    console.log("Jogador 2 morreu.");
}
