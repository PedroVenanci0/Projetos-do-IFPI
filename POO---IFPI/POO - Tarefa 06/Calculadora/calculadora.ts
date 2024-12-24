class Calculadora {
  private operando1: number;
  private operando2: number;

  constructor(operando1: number, operando2: number) {
    this.operando1 = operando1;
    this.operando2 = operando2;
  }

  public somar(): number {
    return this.operando1 + this.operando2;
  }

  public subtrair(): number {
    return this.operando1 - this.operando2;
  }

  public multiplicar(): number {
    return this.operando1 * this.operando2;
  }

  public dividir(): number | string {
    if (this.operando2 === 0) {
      return "Erro: Divisão por zero não é permitida.";
    } else {
      return this.operando1 / this.operando2;
    }
  }
}

const calculadora = new Calculadora(10, 0);

console.log(`Soma: ${calculadora.somar()}`);
console.log(`Subtração: ${calculadora.subtrair()}`);
console.log(`Multiplicação: ${calculadora.multiplicar()}`);
console.log(`Divisão: ${calculadora.dividir()}`);
