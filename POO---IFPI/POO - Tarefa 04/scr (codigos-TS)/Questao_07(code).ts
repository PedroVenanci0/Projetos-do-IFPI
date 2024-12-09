
  class Equipamento { // Definição de uma classe chamada "Equipamento"
    ligado: boolean; // Propriedade "ligado" do tipo boolean

    constructor() { // Construtor que inicializa a propriedade "ligado" da classe
        this.ligado = false; // A propriedade "ligado" é inicializada com o valor padrão "false"
    }

    liga(): void { // Método "liga", que não retorna nada
        if (!this.ligado) { // Verifica se a propriedade "ligado" é false; se for, muda o valor para "true"
            this.ligado = true; // Define "ligado" como true
            console.log("Equipamento ligado."); // Exibe uma mensagem indicando que o equipamento foi ligado
        } else { // Caso "ligado" já seja true, exibe uma mensagem informando que o equipamento já está ligado
            console.log("O equipamento já está ligado.");
        }
    }

    desliga(): void { // Método "desliga", que não retorna nada
        if (this.ligado) { // Verifica se a propriedade "ligado" é true; se for, muda o valor para "false"
            this.ligado = false; // Define "ligado" como false
            console.log("Equipamento desligado."); // Exibe uma mensagem indicando que o equipamento foi desligado
        } else { // Caso "ligado" já seja false, exibe uma mensagem informando que o equipamento já está desligado
            console.log("O equipamento já está desligado.");
        }
    }

    inverte(): void { // Método "inverte", que não retorna nada
        this.ligado = !this.ligado; // Inverte o valor da propriedade "ligado" (true vira false e vice-versa)
        if (this.ligado) { // Verifica se o equipamento está ligado após a inversão
            console.log("Equipamento agora ligado.");
        } else { // Caso contrário, exibe que o equipamento está desligado
            console.log("Equipamento agora desligado.");
        }
    }

    estaLigado(): boolean { // Método que retorna o estado atual do equipamento: true (ligado) ou false (desligado)
        return this.ligado;
    }
}

const meuEquipamento = new Equipamento(); // Criação de um novo objeto da classe "Equipamento"

meuEquipamento.liga(); // Chama o método "liga"; o equipamento passa a estar "ligado" (true)
meuEquipamento.liga(); // Chama o método "liga" novamente; informa que o equipamento já está ligado
meuEquipamento.desliga(); // Chama o método "desliga"; o equipamento passa a estar "desligado" (false)
meuEquipamento.desliga(); // Chama o método "desliga" novamente; informa que o equipamento já está desligado

meuEquipamento.inverte(); // Chama o método "inverte"; altera o estado para "ligado" (true)
meuEquipamento.inverte(); // Chama o método "inverte" novamente; altera o estado para "desligado" (false)

console.log("Está ligado?", meuEquipamento.estaLigado()); // Exibe no console o estado atual do equipamento concatenado com uma mensagem
