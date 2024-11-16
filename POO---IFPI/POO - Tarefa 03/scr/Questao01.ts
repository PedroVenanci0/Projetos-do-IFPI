 
class identificandoNumero{
    numero: number

    constructor(numero: number){
        this.numero = numero
    }

    verificarNumero(): string{
        if (this.numero % 2 == 0)
            return "Esse numero é par"
        else{
            return "Esse numero é impar"
        }
    }
}

const numeroObj = new identificandoNumero(22)

console.log(numeroObj.verificarNumero())