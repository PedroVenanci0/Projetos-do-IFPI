class Hora {
    private hora: number;
    private minutos: number;
    private segundos: number;
  
    constructor(hora: number, minutos: number, segundos: number) {
      this.hora = hora;
      this.minutos = minutos;
      this.segundos = segundos;
    }
  
    public lerHora(): number {
      return this.hora;
    }
  
    public lerMinutos(): number {
      return this.minutos;
    }
  
    public lerSegundos(): number {
      return this.segundos;
    }
  
    public mostrarHora(): string {
      const horaFormatada = this.hora.toString().padStart(2, "0");
      const minutosFormatados = this.minutos.toString().padStart(2, "0");
      const segundosFormatados = this.segundos.toString().padStart(2, "0");
  
      return `${horaFormatada}:${minutosFormatados}:${segundosFormatados}`;
    }
  }
  
  // Instância da classe Hora
  const minhaHora = new Hora(9, 5, 30);
  
  // Exibe a hora formatada
  console.log("Hora atual formatada:", minhaHora.mostrarHora());
  