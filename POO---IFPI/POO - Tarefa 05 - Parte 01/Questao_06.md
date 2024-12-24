

## a. Você concorda que o banco faz o cadastro de duas entidades e ainda faz regras de negócios?

Não, eu acho que essas responsabilidades deviam ser separadas. Cada entidade deveria cuidar das suas próprias regras. O banco deve ser mais como um organizador, facilitando a interação entre as entidades, mas não fazendo validações ou controlando regras de negócio complicadas.

## b. Não seria adequado o banco ter uma classe CadastroDeClientes e CadastroDeContas e algumas regras de validação serem feitas no banco e deixar os métodos de consulta e inclusão os mais simples possíveis?

Sim, faz sentido. O banco poderia só cuidar das consultas e inclusões, enquanto as validações ficariam nas classes de CadastroDeClientes e CadastroDeContas. Assim, o banco fica mais simples e as regras de negócio ficam centralizadas no lugar certo.

## c. O método associar cliente a uma conta deveria estar em que classe? Banco, CadastroDeContas ou CadastroDeClientes?

Esse método deveria estar na classe Banco, porque é ela que gerencia tanto os clientes quanto as contas, então é a mais indicada para fazer essa associação.
