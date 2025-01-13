// Importando a classe Calculadora do arquivo Questão_02
import { Calculadora } from './Questão_02';

class CalculadoraCientifica extends Calculadora {
  exponenciar(): number {
    // Acessando os atributos através de métodos herdados ou usando propriedades protegidas
    const base = (this as any).operando1;
    const expoente = (this as any).operando2;
    return Math.pow(base, expoente);
  }
}

// Testando a CalculadoraCientifica
const calcCientifica = new CalculadoraCientifica(2, 3);
console.log(`Soma: ${calcCientifica.soma()}`); // Saída: Soma: 5
console.log(`Exponenciação: ${calcCientifica.exponenciar()}`); // Saída: Exponenciação: 8
