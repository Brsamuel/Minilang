class Generator:
 
    # =========================
    # GERAR EXPRESSÕES
    # =========================
 
    def generate_expression(self, expr):
        # OPERAÇÃO MATEMÁTICA
        if isinstance(expr, dict) and expr.get("type") == "BINARY_OP":
            left = self.generate_expression(expr["left"])
            operator = expr["operator"]
            right = self.generate_expression(expr["right"])
            return f'({left} {operator} {right})'
        # NÚMERO OU VARIÁVEL
        else:
            return str(expr)
 
    # =========================
    # GERAR LISTA DE STATEMENTS (recursivo, com indentação)
    # =========================
 
    def generate_statements(self, statements, indent=0):
        prefix = '    ' * indent
        code = ''
        for node in statements:
            code += self.generate_node(node, indent)
        return code
 
    # =========================
    # GERAR UM NÓ (comando individual)
    # =========================
 
    def generate_node(self, node, indent=0):
        prefix = '    ' * indent
        code = ''
 
        # =========================
        # PRINT
        # =========================
        if node["type"] == "PRINT":
            value = node["value"]
            value_type = node["value_type"]
            if value_type == "STRING":
                code += f'{prefix}print("{value}")\n'
            elif value_type == "VARIABLE":
                code += f'{prefix}print({value})\n'
 
        # =========================
        # LET
        # =========================
        elif node["type"] == "LET":
            name = node["name"]
            value = node["value"]
            if isinstance(value, str) and not isinstance(value, dict):
                code += f'{prefix}{name} = "{value}"\n'
            else:
                expression = self.generate_expression(value)
                code += f'{prefix}{name} = {expression}\n'
 
        # =========================
        # IF
        # =========================
        elif node["type"] == "IF":
            left = self.generate_expression(node["left"])
            operator = node["operator"]
            right = self.generate_expression(node["right"])
            code += f'{prefix}if {left} {operator} {right}:\n'
            code += self.generate_statements(node["body"], indent + 1)
 
            for elif_node in node["elifs"]:
                left = self.generate_expression(elif_node["left"])
                operator = elif_node["operator"]
                right = self.generate_expression(elif_node["right"])
                code += f'{prefix}elif {left} {operator} {right}:\n'
                code += self.generate_statements(elif_node["body"], indent + 1)
 
            if node["else"] is not None:
                code += f'{prefix}else:\n'
                code += self.generate_statements(node["else"], indent + 1)
 
        # =========================
        # FOR
        # =========================
        elif node["type"] == "FOR":
            variable = node["variable"]
            start = self.generate_expression(node["start"])
            end = self.generate_expression(node["end"])
            code += f'{prefix}for {variable} in range({start}, ({end}) + 1):\n'
            code += self.generate_statements(node["body"], indent + 1)
 
        # =========================
        # WHILE
        # =========================
        elif node["type"] == "WHILE":
            left = self.generate_expression(node["left"])
            operator = node["operator"]
            right = self.generate_expression(node["right"])
            code += f'{prefix}while {left} {operator} {right}:\n'
            code += self.generate_statements(node["body"], indent + 1)
 
        return code
 
    # =========================
    # GERAR CÓDIGO (entrada principal)
    # =========================
 
    def generate(self, ast):
        return self.generate_statements(ast, indent=0)