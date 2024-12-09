
Alternativa A)

Antes de configurar o outDir, os arquivos JavaScript gerados ficavam misturados com os arquivos TypeScript no mesmo diretório. Agora, eles serão separados, deixando seu projeto mais organizado

Alternativa B)

Com "allowUmdGlobalAccess": true: Você pode acessar variáveis globais definidas por bibliotecas UMD no seu código TypeScript.
Sem "allowUmdGlobalAccess": true: Você não pode acessar essas variáveis globais diretamente, e o TypeScript vai gerar um erro se tentar usar algo que não foi explicitamente importado.


Alternativa C)

A configuração noImplicitAny no TypeScript é usada para ajudar a prevenir o uso implícito do tipo any. Quando ela está definida como true, o compilador do TypeScript exigirá que você seja explícito ao declarar tipos, reduzindo a possibilidade de erros relacionados a tipagem desconhecida.

Alternativa D)

Ao transpilar com o target: ES3, o código gerado será compatível com navegadores antigos e ficará mais verboso


Alternativa E)

A configuração strictNullChecks no TypeScript, quando definida como true, faz com que o compilador trate null e undefined como tipos distintos de outros tipos. Isso significa que você precisa ser explícito ao permitir valores null ou undefined em suas variáveis ou parâmetros. Essa configuração ajuda a evitar erros comuns relacionados a valores nulos.