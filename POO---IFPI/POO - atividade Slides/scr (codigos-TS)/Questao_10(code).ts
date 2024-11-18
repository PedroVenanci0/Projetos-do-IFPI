class Jogador {
    private forca: number;
    private nivel: number;
    private pontos: number;

    constructor(forca: number, nivel: number, pontos: number) {
        this.forca = forca;
        this.nivel = nivel;
        this.pontos = pontos;
    }

    calcularAtaque(): number {
        return this.forca * this.nivel;
    }


    atacar(jogadorAtacado: Jogador): void {
        if (jogadorAtacado.estaVivo()) {
            const dano = this.calcularAtaque();
            jogadorAtacado.receberDano(dano);
            console.log(`${this.toString()} atacou ${jogadorAtacado.toString()} causando ${dano} de dano.`);
        } else {
            console.log(`${jogadorAtacado.toString()} não pode ser atacado, pois já está morto.`);
        }
    }


    estaVivo(): boolean {
        return this.pontos > 0;
    }

    private receberDano(dano: number): void {
        this.pontos -= dano;
    }

    toString(): string {
        return `Jogador [Força: ${this.forca}, Nível: ${this.nivel}, Pontos: ${this.pontos}]`;
    }
}


let jogador1 = new Jogador(10, 5, 100); 
let jogador2 = new Jogador(8, 4, 100);  

jogador1.atacar(jogador2);  

jogador2.atacar(jogador1);  

console.log(jogador1.toString());  
console.log(jogador2.toString());  

if (jogador1.estaVivo()) {
    console.log("Jogador 1 está vivo!");
} else {
    console.log("Jogador 1 morreu.");
}

if (jogador2.estaVivo()) {
    console.log("Jogador 2 está vivo!");
} else {
    console.log("Jogador 2 morreu.");
}
