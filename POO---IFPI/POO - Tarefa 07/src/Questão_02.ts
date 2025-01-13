// Exportando a classe Calculadora para ser usada em outros arquivos
export class Calculadora {
    private operando1: number;
    private operando2: number;
  
    constructor(operando1: number, operando2: number) {
      this.operando1 = operando1;
      this.operando2 = operando2;
    }
  
    soma(): number {
      return this.operando1 + this.operando2;
    }
  }
  
  // Testando a classe Calculadora
  const calc = new Calculadora(10, 20);
  console.log(`Soma: ${calc.soma()}`); // Saída: Soma: 30
  