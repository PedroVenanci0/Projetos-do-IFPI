class Hotel {
    quantReservas: number;
    constructor(quantReservas: number = 0) {
      this.quantReservas = quantReservas;
    }
  
    adicionarReserva(): void {
      this.quantReservas++;
    }
  }
  
  let hotel: Hotel = new Hotel(2); 
  console.log(hotel.quantReservas); 
  