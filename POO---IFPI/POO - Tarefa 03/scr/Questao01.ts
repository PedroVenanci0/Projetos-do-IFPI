 
class identificandoNumero{ // Cria uma classe chamada identificandoNumero e define como propriedade o numero do tipo number
    numero: number

    constructor(numero: number){ // Temos a iniciacialização das propriedades da classe professor por meio do contrutor
        this.numero = numero
    }

    verificarNumero(): string{ // Na classe identificarNumero temos o metodo verificarNumero que nao recebe nenhum paremetro mas nos devolve se o 
        if (this.numero % 2 == 0) // numero correspondente é par ou impar
            return "Esse numero é par"
        else{
            return "Esse numero é impar"
        }
    }
}

const numeroObj = new identificandoNumero(22) // Aqui temos a criação de uma nova instancia da classe identificando numero

console.log(numeroObj.verificarNumero()) // aqui temos a utilização do metodo verificandoNumero