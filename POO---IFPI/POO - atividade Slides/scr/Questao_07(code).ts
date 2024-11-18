class Equipamento {
    ligado: boolean;
  
    constructor() {
      this.ligado = false;
    }
  
    liga(): void {
      if (!this.ligado) {
        this.ligado = true;
        console.log("Equipamento ligado.");
      } else {
        console.log("O equipamento já está ligado.");
      }
    }
  
    desliga(): void {
      if (this.ligado) {
        this.ligado = false;
        console.log("Equipamento desligado.");
      } else {
        console.log("O equipamento já está desligado.");
      }
    }
  
    inverte(): void {
      this.ligado = !this.ligado;
      if (this.ligado) {
        console.log("Equipamento agora ligado.");
      } else {
        console.log("Equipamento agora desligado.");
      }
    }
  
    estaLigado(): boolean {
      return this.ligado;
    }
  }
  
  const meuEquipamento = new Equipamento();
  
  meuEquipamento.liga();
  meuEquipamento.liga();
  meuEquipamento.desliga();
  meuEquipamento.desliga();
  
  meuEquipamento.inverte();
  meuEquipamento.inverte();
  
  console.log("Está ligado?", meuEquipamento.estaLigado()); 
  