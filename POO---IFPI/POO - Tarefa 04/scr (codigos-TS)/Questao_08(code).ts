class Conta { // Definição da classe "Conta"
  numero: string; // Propriedade "numero" para armazenar o número da conta, do tipo string
  saldo: number; // Propriedade "saldo" para armazenar o saldo da conta, do tipo number

  constructor(numero: string, saldo: number) { // Construtor que inicializa as propriedades "numero" e "saldo"
      this.numero = numero; // Atribui o valor recebido no parâmetro "numero" à propriedade "numero"
      this.saldo = saldo; // Atribui o valor recebido no parâmetro "saldo" à propriedade "saldo"
  }

  sacar(valor: number): boolean { // Método "sacar", que tenta debitar um valor do saldo, retornando true ou false
      if (valor <= this.saldo) { // Verifica se o valor a ser sacado é menor ou igual ao saldo disponível
          this.saldo -= valor; // Se a condição for verdadeira, o saldo é reduzido pelo valor sacado
          return true; // Retorna true para indicar que o saque foi bem-sucedido
      }
      return false; // Retorna false se o saldo for insuficiente
  }

  transferir(contaDestino: Conta, valor: number): boolean { // Método "transferir", que tenta transferir um valor para outra conta
      if (this.sacar(valor)) { // Verifica se o saque foi realizado com sucesso
          contaDestino.saldo += valor; // Adiciona o valor transferido ao saldo da conta de destino
          return true; // Retorna true para indicar que a transferência foi bem-sucedida
      }
      return false; // Retorna false se o saque não puder ser realizado
  }

  consultarSaldo(): number { // Método "consultarSaldo" que retorna o saldo atual da conta
      return this.saldo;
  }
}

// Criação de dois objetos da classe "Conta" com números e saldos iniciais
let conta1 = new Conta("1", 100); // Conta 1 com saldo inicial de 100
let conta2 = new Conta("2", 50); // Conta 2 com saldo inicial de 50

// Operações realizadas nas contas
console.log(conta1.sacar(30)); // Tenta sacar 30 da conta1; deve retornar true (saldo suficiente)
console.log(conta1.sacar(80)); // Tenta sacar 80 da conta1; deve retornar false (saldo insuficiente)
console.log(conta1.transferir(conta2, 50)); // Tenta transferir 50 de conta1 para conta2; deve retornar true
console.log(conta1.transferir(conta2, 200)); // Tenta transferir 200 de conta1 para conta2; deve retornar false

// Exibe os saldos finais de conta1 e conta2
console.log(conta1.consultarSaldo()); // Saldo final de conta1 após as operações
console.log(conta2.consultarSaldo()); // Saldo final de conta2 após as operações
