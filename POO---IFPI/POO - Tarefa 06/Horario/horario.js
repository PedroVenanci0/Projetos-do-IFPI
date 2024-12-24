"use strict";
class Hora {
    constructor(hora, minutos, segundos) {
        this.hora = hora;
        this.minutos = minutos;
        this.segundos = segundos;
    }
    lerHora() {
        return this.hora;
    }
    lerMinutos() {
        return this.minutos;
    }
    lerSegundos() {
        return this.segundos;
    }
    mostrarHora() {
        const horaFormatada = this.hora.toString().padStart(2, '0');
        const minutosFormatados = this.minutos.toString().padStart(2, '0');
        const segundosFormatados = this.segundos.toString().padStart(2, '0');
        return `${horaFormatada}:${minutosFormatados}:${segundosFormatados}`;
    }
}
const minhaHora = new Hora(9, 5, 30);
// console.log(minhaHora.lerHora())       
// console.log(minhaHora.lerMinutos())     
// console.log(minhaHora.lerSegundos())
console.log(minhaHora.mostrarHora());
