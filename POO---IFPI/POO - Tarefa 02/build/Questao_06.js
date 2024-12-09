//6. Reescreva o exemplo abaixo, mantendo a quebra de linhas usando template
//strings e os valores Ely, 120.56 e TypeScript venham de variáveis declaradas
//separadamente e “interpoladas” na string:
//Ely
//My payment time is 120.56
//and
//my preffered language is TypeScript
var Professor = /** @class */ (function () {
    function Professor(nome, pagamento, linguagem) {
        this.nome = nome;
        this.pagamento = pagamento;
        this.linguagem = linguagem;
    }
    Professor.prototype.saudacao = function () {
        console.log("".concat(this.nome, "\nMy payment time is ").concat(this.pagamento, "\nand\nmy preferred language is ").concat(this.linguagem));
    };
    return Professor;
}());
var nome = "Ely";
var pagamento = 120.56;
var linguagem = "TypeScript";
var professor = new Professor(nome, pagamento, linguagem);
professor.saudacao();
