//6. Reescreva o exemplo abaixo, mantendo a quebra de linhas usando template
//strings e os valores Ely, 120.56 e TypeScript venham de variáveis declaradas
//separadamente e “interpoladas” na string:

//Ely
//My payment time is 120.56
//and
//my preffered language is TypeScript

class Professor {
    nome: string;
    pagamento: number;
    linguagem: string;

    constructor(nome: string, pagamento: number, linguagem: string) {
        this.nome = nome;
        this.pagamento = pagamento;
        this.linguagem = linguagem;
    }
    saudacao() {
        console.log(`${this.nome}
My payment time is ${this.pagamento}
and
my preferred language is ${this.linguagem}`);
    }
}
const nome = "Ely";
const pagamento = 120.56;
const linguagem = "TypeScript";

const professor = new Professor(nome, pagamento, linguagem);
professor.saudacao();


