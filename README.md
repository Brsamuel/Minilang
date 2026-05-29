# Mini Compiler

Compilador educacional desenvolvido em Python para a disciplina de Compiladores.

## Funcionalidades

- PRINT
- LET
- IF
- FOR

## Estrutura do Projeto

- Lexer
- Parser
- AST
- Generator

## Exemplo de Código

### Entrada
## Comandos Disponíveis

| Comando | Função |
|---|---|
| PRINT | Exibe mensagens ou variáveis |
| LET | Cria variáveis |
| IF | Estrutura condicional |
| FOR | Estrutura de repetição |
| END | Finaliza blocos IF e FOR |

## Sintaxe da Linguagem em exemplos

### PRINT
```txt
PRINT "Olá mundo"
```

```txt
PRINT "Olá"
PRINT variavel
```

# Operações Matemáticas

```txt
Operações Matemáticas
LET a = 10
LET b = 5

LET soma = a + b
LET sub = a - b
LET mult = a * b
LET div = a / b

PRINT soma
PRINT sub
PRINT mult
PRINT div
```


### LET

```txt
LET nome = "Brian"
LET idade = 22
```

### IF

```txt
IF idade > 18
PRINT "Maior de idade"
END
```
```
LET idade = 15

IF idade > 17
PRINT "Maior de idade"

ELSE
PRINT "Menor de idade"

END
```
```
IF + ELIF + ELSE
LET nota = 7

IF nota > 7
PRINT "Aprovado"

ELIF nota == 7
PRINT "Passou na média"

ELSE
PRINT "Reprovado"

END
```

### FOR

```txt
FOR i = 1 TO 5
PRINT i
END
```

Os códigos podem ser inseridos no "programa.mini" e ao salvar(Crtl + S) clica em executar no "main.py". 

A saída gerada vai ser apresentada em "Output.py". 

### Saída Gerada

```python
for i in range(1, 6):
    print(i)
```

### Funcionalidades

Variáveis
Strings
Operações matemáticas
IF / ELIF / ELSE
FOR loops
AST
Lexer com PLY
Parser LALR com PLY
Geração de código Python

## Como Executar

primeiro, instala o ply

```bash
pip install ply
```

```bash
python main.py
```

## Tecnologias Utilizadas

- Python
- Git
- GitHub
- VS Code

