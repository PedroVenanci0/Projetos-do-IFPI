class Conta_ {
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

  let conta01 = new Conta("1", 100);
  let conta02 = new Conta("2", 50);
  
 
  console.log(conta01.sacar(30)); 
  console.log(conta01.sacar(80)); 
  console.log(conta01.transferir(conta02, 50)); 
  console.log(conta01.transferir(conta02, 200));
  
  console.log(conta01.consultarSaldo()); 
  console.log(conta02.consultarSaldo()); 
  