# Mini Compiler

Compilador educacional desenvolvido em Python para a disciplina de Compiladores.

### Alunos

```txt

Ryan Nunes da Silva - 01431101
Anderson Djalma Santos Pinto - 01607677
Gabriel de Oliveira Barros - 01608601
Brian Samuel de Barros Santos - 01608705
```

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

### Exemplos variados
```txt
LET nome = "Minilang"
PRINT "=== Bem-vindo ao compilador"
PRINT nome
```

```txt
LET a = 10
LET b = 3
LET soma = a + b
LET sub = a - b
LET mult = a * b
LET div = a / b
PRINT "--- Operacoes Matematicas ---"
PRINT soma
PRINT sub
PRINT mult
PRINT div
```

```txt
PRINT "--- FOR loop ---"
FOR i = 1 TO 5
PRINT i
END
```

```txt
PRINT "--- WHILE loop ---"
LET x = 1
WHILE x < 6
PRINT x
LET x = x + 1
END
```

```txt
PRINT "--- IF simples ---"
LET idade = 20
IF idade >= 18
PRINT "Maior de idade"
END
```

```txt
PRINT "--- IF ELSE ---"
LET nota = 5
IF nota >= 7
PRINT "Aprovado"
ELSE
PRINT "Reprovado"
END
```

```txt
PRINT "--- IF ELIF ELSE ---"
LET pontos = 7
IF pontos > 7
PRINT "Aprovado"
ELIF pontos == 7
PRINT "Passou na media"
ELSE
PRINT "Reprovado"
END
```

```txt
PRINT "--- LET dentro de IF ---"
LET valor = 10
IF valor > 5
LET dobro = valor + valor
PRINT dobro
END
```

```txt
PRINT "--- FOR com operacao dentro ---"
FOR j = 1 TO 3
LET quadrado = j * j
PRINT quadrado
END
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

