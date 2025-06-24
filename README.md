## Programa Verificador da Sintaxe da Linguagem

O parser foi implementado na linguagem Python, seguindo o modelo de um analisador descendente preditivo baseado na gramática LL(1) construída

## Funcionalidades

O parser reconhece e valida expressões com:

- **Operadores Booleanos**: `|` (OR), `&` (AND)
- **Operadores de Igualdade**: `=` (igual), `~` (diferente)
- **Operadores Relacionais**: `<` (menor que), `>` (maior que)
- **Operadores Aritméticos**: `+` (soma), `-` (subtração), `*` (multiplicação), `/` (divisão)
- **Operadores Unários**: `!` (negação), `-` (menos unário), `+` (mais unário)
- **Variáveis**: `a`, `b`, `c`, `t`, `f`
- **Números**: dígitos de 0-9
- **Parênteses**: `(` e `)` para agrupamento

## Gramática

O parser implementa a seguinte hierarquia de precedência (do menor para o maior):

1. `BOOL` → `JOIN` (`|` `JOIN`)*
2. `JOIN` → `EQUAL` (`&` `EQUAL`)*
3. `EQUAL` → `REL` (`=`|`~` `REL`)*
4. `REL` → `EXPR` (`<`|`>` `EXPR`)*
5. `EXPR` → `TERM` (`+`|`-` `TERM`)*
6. `TERM` → `UNARY` (`*`|`/` `UNARY`)*
7. `UNARY` → (`!`|`-`|`+`) `UNARY` | `FACTOR`
8. `FACTOR` → `(` `BOOL` `)` | variável | número

## Como Executar

### Pré-requisitos

- Python 3.x instalado no sistema

### Execução

1. **Navegue até o diretório do projeto:**

2. **Execute o arquivo Python:**
parser.py
  
### Exemplos de Uso

O código já inclui alguns exemplos que são executados automaticamente:

exemplos = ["a|b", "!(a=b)&f", "(a+b)>fdfc"]

**Saída esperada:**
```
Entrada 'a|b': Aceita!
Entrada '!(a=b)&f': Aceita!
Entrada '(a+b)>fdfc': Rejeitada! Erro: Entrada restante não consumida a partir do index 8.