//6. Reescreva o exemplo abaixo, mantendo a quebra de linhas usando template
//strings e os valores Ely, 120.56 e TypeScript venham de variáveis declaradas
//separadamente e “interpoladas” na string:

//Ely
//My payment time is 120.56
//and
//my preffered language is TypeScript

class Professor {

    // Aqui, estamos criando uma classe chamada Professor. Em TypeScript (e JavaScript), 
    // uma classe é uma estrutura que permite criar objetos com propriedades e métodos, 
    // que podem ser usados para representar comportamentos ou características de uma entidade.

    nome: string;
    pagamento: number;
    linguagem: string;

    // Estas são propriedades da classe Professor. Elas são definidas diretamente dentro da classe e têm os tipos explicitados:

    // nome: string → A propriedade nome será uma string.
    // pagamento: number → A propriedade pagamento será um número (provavelmente um valor monetário).
    // linguagem: string → A propriedade linguagem será uma string (representando a linguagem de programação preferida do professor).
    // Essas propriedades são definidas, mas não inicializadas até que a classe seja instanciada.
    

    constructor(nome: string, pagamento: number, linguagem: string) {
        this.nome = nome;
        this.pagamento = pagamento;
        this.linguagem = linguagem;
    }

    // Aqui temos o construtor da classe Professor. 
    // O construtor é um método especial que é chamado automaticamente quando você cria uma nova instância da classe. 
    // Ele é responsável por inicializar as propriedades da classe.

    // O constructor(nome: string, pagamento: number, linguagem: string) recebe três parâmetros: nome, pagamento e linguagem, 
    // e os usa para inicializar as propriedades correspondentes da instância (this.nome, this.pagamento e this.linguagem).
    // this é uma referência à instância atual do objeto. 
    // Portanto, o this.nome = nome; está atribuindo o valor do parâmetro nome à propriedade nome da instância.

    saudacao() {
        console.log(`${this.nome}
My payment time is ${this.pagamento}
and
my preferred language is ${this.linguagem}`);
    }
}

// Este é um método da classe Professor. 
// O método saudacao não recebe parâmetros, mas usa as propriedades da instância (this.nome, this.pagamento e this.linguagem) 
// para imprimir uma mensagem de saudação no console.

const nome = "Ely";
const pagamento = 120.56;
const linguagem = "TypeScript";

const professor = new Professor(nome, pagamento, linguagem);
professor.saudacao();

// Aqui, estamos criando uma instância da classe Professor e utilizando o método saudacao:

// Criando variáveis: nome, pagamento e linguagem são variáveis que armazenam os valores que serão passados para a instância do Professor.

// Instanciando a classe: const professor = new Professor(nome, pagamento, linguagem);

// Aqui estamos criando um novo objeto professor da classe Professor. O operador new é usado para criar uma nova instância de uma classe.
// Os valores de nome, pagamento e linguagem são passados para o construtor da classe, o que inicializa as propriedades da instância.
// Chamando o método saudacao: professor.saudacao();

// Depois de criar a instância, chamamos o método saudacao que irá imprimir a mensagem formatada com as propriedades da instância do professor.


