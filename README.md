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
PRINT "Olá"
PRINT variavel
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

## Como Executar

```bash
python main.py
```

## Tecnologias Utilizadas

- Python
- Git
- GitHub
- VS Code

