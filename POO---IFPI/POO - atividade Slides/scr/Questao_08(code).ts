class Conta {
    numero: string;
    saldo: number;
  
    constructor(numero: string, saldo: number) {
      this.numero = numero;
      this.saldo = saldo;
    }
  
    sacar(valor: number): boolean {
      if (valor <= this.saldo) {
        this.saldo -= valor;
        return true; 
      }
      return false; 
    }
  
    transferir(contaDestino: Conta, valor: number): boolean {
      if (this.sacar(valor)) {
        contaDestino.saldo += valor;
        return true; 
      }
      return false;
    }
  
    consultarSaldo(): number {
      return this.saldo;
    }
  }
  
  let conta1 = new Conta("1", 100);
  let conta2 = new Conta("2", 50);
  
  console.log(conta1.sacar(30)); 
  console.log(conta1.sacar(80)); 
  console.log(conta1.transferir(conta2, 50)); 
  console.log(conta1.transferir(conta2, 200)); 
  
  console.log(conta1.consultarSaldo());
  console.log(conta2.consultarSaldo());
  