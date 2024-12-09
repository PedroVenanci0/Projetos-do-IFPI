class Conta_ { // Definição de uma classe chamada "Conta_"
  numero: string; // Propriedade "numero" para identificar a conta, do tipo string
  saldo: number; // Propriedade "saldo" para armazenar o valor atual na conta, do tipo number

  constructor(numero: string, saldo: number) { // Construtor para inicializar as propriedades "numero" e "saldo"
      this.numero = numero; // Atribui o valor recebido no parâmetro "numero" à propriedade da classe
      this.saldo = saldo; // Atribui o valor recebido no parâmetro "saldo" à propriedade da classe
  }

  sacar(valor: number): boolean { // Método "sacar" que tenta retirar um valor do saldo
      if (valor <= this.saldo) { // Verifica se há saldo suficiente para realizar o saque
          this.saldo -= valor; // Subtrai o valor do saldo
          return true; // Retorna true para indicar que o saque foi realizado
      }
      return false; // Retorna false se o saldo for insuficiente
  }

  transferir(contaDestino: Conta_, valor: number): boolean { // Método "transferir" que realiza uma transferência para outra conta
      if (this.sacar(valor)) { // Tenta realizar o saque do valor da conta atual
          contaDestino.saldo += valor; // Adiciona o valor transferido ao saldo da conta de destino
          return true; // Retorna true para indicar que a transferência foi bem-sucedida
      }
      return false; // Retorna false se o saque não foi realizado (saldo insuficiente)
  }

  consultarSaldo(): number { // Método que retorna o saldo atual da conta
      return this.saldo;
  }
}

// Criação de dois objetos da classe "Conta_" com valores iniciais
let conta01 = new Conta_("1", 100); // Conta com número "1" e saldo inicial de 100
let conta02 = new Conta_("2", 50); // Conta com número "2" e saldo inicial de 50

// Operações de saque e transferência entre as contas
console.log(conta01.sacar(30)); // Tenta sacar 30 de conta01; deve retornar true (saldo suficiente)
console.log(conta01.sacar(80)); // Tenta sacar 80 de conta01; deve retornar false (saldo insuficiente)
console.log(conta01.transferir(conta02, 50)); // Tenta transferir 50 de conta01 para conta02; deve retornar true
console.log(conta01.transferir(conta02, 200)); // Tenta transferir 200 de conta01 para conta02; deve retornar false (saldo insuficiente)

// Exibe os saldos finais de cada conta após as operações realizadas
console.log(conta01.consultarSaldo()); // Retorna o saldo final de conta01 (20, após os saques e transferências)
console.log(conta02.consultarSaldo()); // Retorna o saldo final de conta02 (100, após receber a transferência)
