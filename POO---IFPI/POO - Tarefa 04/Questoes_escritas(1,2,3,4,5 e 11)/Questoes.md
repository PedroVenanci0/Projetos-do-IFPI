

1. Assinale verdadeiro ou falso:

(F) Objetos são modelos para classes;
(F) Atributos de uma classe devem ser obrigatoriamente inicializados para que as
classes compilem;
(V) Uma variável declarada dentro de um método deve ser inicializada para que a
classe seja compilável;
(F) Uma variável que seja uma classe declarada em um método é automaticamente
inicializada com undefined;
(V) Construtores são rotinas especiais que servem para inicializar e configurar os
objetos no momento da instanciação;
(V) Construtores não possuem tipo de retorno e podem ou não ter parâmetros;
(V) Uma classe pode ter várias instâncias.
_____________________________________________________________________________

2. Suponha uma classe Hotel que sirva apenas para guardar a quantidade de
solicitações de reservas feitas conforme abaixo:

class Hotel {
quantReservas : number;
adicionarReserva() : void {
this.quantReservas++;
}
}

Podemos afirmar que haverá um problema de compilação, pois a variável inteira não
foi inicializada previamente? Justifique.

RESPOSTA: Sim, pois ao usar this.quantReservas++ sem inicializar quantReservas, ocorre um erro porque o atributo está declarado, mas não tem valor definido.

_____________________________________________________________________________

3. Ainda sobre a classe do exemplo anterior, considere o código abaixo:
let hotel : Hotel = new Hotel(2);
console.log(hotel.quantReservas);

Adicione o construtor que aceite um parâmetro inteiro e faça a inicialização do atributo
quantReservas.

Resposta: 

class Hotel {
  quantReservas: number;

  // Construtor que aceita um parâmetro inteiro
  constructor(quantReservas: number) {
    this.quantReservas = quantReservas;
  }

  adicionarReserva(): void {
    this.quantReservas++;
  }
}
let hotel: Hotel = new Hotel(2); 
console.log(hotel.quantReservas); 

_____________________________________________________________________________

4. Considere a classe Radio e as instruções que fazem seu uso abaixo:
class Radio {
volume : number;
constructor(volume : number) {
this.volume = volume;

}
}
let r : Radio = new Radio();
r.volume = 10;
Justifique o erro de compilação e proponha uma solução.


Resposta:

O erro ocorreu por conta que o objeto Radio nao recebe nenhum argumento

_____________________________________________________________________________

5. Considerando o uso da classe Conta apresentada em aula e seu uso abaixo:
let c1: Conta = new Conta("1",100);
let c2: Conta = new Conta("2",100);
let c3: Conta;
c1 = c2;
c3 = c1;
c1.sacar(10);
c1.transferir(c2,50);
console.log(c1.consultarSaldo());
console.log(c2.consultarSaldo());
console.log(c3.consultarSaldo());
a. Qual o resultado dos dois "prints"? Justifique sua resposta.
b. O que acontece com o objeto para o qual a referência c1 apontava?

Resposta:

a/ Nos dois "prints" apresentados, os resultados são 90, pois, no momento do código onde há saque e transferência, as variáveis apontam para a mesma referência, fazendo com que tenham comportamentos de saque e transferência iguais. Ou seja, ao transferir 50 de c1 para c2, acaba que c2 também transfere 50 para c1, fazendo com que os valores permaneçam inalterados. Já no saque, como c1 saca 10, c2 também saca 10, fazendo com que as duas variáveis terminem com 90.

b/ Quando c1 passa a apontar para c2, a referência original de c1 se perde, fazendo com que o sistema eventualmente a descarte.

_____________________________________________________________________________

11. Na Questão 9, temos um código mais aberto a feedback para o usuario, como quando falamos se é possivel transferir e sacar o valor por meio
do true e false, ja na questao 10 temos um código que o proprio objeto gerencia sua consistência.
