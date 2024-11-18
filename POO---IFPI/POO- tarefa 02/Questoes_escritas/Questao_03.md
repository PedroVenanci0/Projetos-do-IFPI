3 - Pesquise um exemplo na internet em que a tipagem dinâmica pode ser problemático.

Imagine a seguinte situação: trabalhamos em um sistema importantíssimo de finanças pessoais. 
Nele, a pessoa digita quanto ganha e quanto gasta e nós vamos adicionando e subtraindo esses valores de seu saldo.
Após uma atualização no nosso sistema, recebemos uma ligação desesperada do comercial da empresa: 
tem uns valores muito loucos aparecendo para os clientes e as contas não batem.
Nessa atualização permitimos que os números sejam retirados diretamente da conta corrente do cliente. 
O que não havíamos percebido é que esses valores vinham como String e não estávamos tratando isso. 
Sendo assim, um valor de R$20,00 que entrou em uma conta com mais R$20,00 fez com que essa conta totalizasse R$2020,00!


