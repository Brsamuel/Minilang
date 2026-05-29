class Generator:

    # =========================
    # GERAR EXPRESSÕES
    # =========================

    def generate_expression(self, expr):

        # OPERAÇÃO MATEMÁTICA
        if isinstance(expr, dict):

            left = self.generate_expression(expr["left"])

            operator = expr["operator"]

            right = self.generate_expression(expr["right"])

            return f'({left} {operator} {right})'

        # NÚMERO OU VARIÁVEL
        else:

            return str(expr)

    # =========================
    # GERAR CÓDIGO
    # =========================

    def generate(self, ast):

        python_code = ""

        for node in ast:

            # =========================
            # PRINT
            # =========================

            if node["type"] == "PRINT":

                value = node["value"]

                value_type = node["value_type"]

                # STRING
                if value_type == "STRING":

                    python_code += f'print("{value}")\n'

                # VARIÁVEL
                elif value_type == "VARIABLE":

                    python_code += f'print({value})\n'

            # =========================
            # LET
            # =========================

            elif node["type"] == "LET":

                name = node["name"]

                value = node["value"]

                # STRING
                if isinstance(value, str) and not isinstance(value, dict):

                    python_code += f'{name} = "{value}"\n'

                # EXPRESSÃO / NÚMERO
                else:

                    expression = self.generate_expression(value)

                    python_code += f'{name} = {expression}\n'

            # =========================
            # IF
            # =========================

            elif node["type"] == "IF":

                left = self.generate_expression(node["left"])

                operator = node["operator"]

                right = self.generate_expression(node["right"])

                python_code += f'if {left} {operator} {right}:\n'

                for body_node in node["body"]:

                    if body_node["type"] == "PRINT":

                        value = body_node["value"]

                        value_type = body_node["value_type"]

                        if value_type == "STRING":

                            python_code += f'    print("{value}")\n'

                        elif value_type == "VARIABLE":

                            python_code += f'    print({value})\n'

                # ELIFS
                for elif_node in node["elifs"]:

                    left = self.generate_expression(elif_node["left"])

                    operator = elif_node["operator"]

                    right = self.generate_expression(elif_node["right"])

                    python_code += f'elif {left} {operator} {right}:\n'

                    for body_node in elif_node["body"]:

                        if body_node["type"] == "PRINT":

                            value = body_node["value"]

                            value_type = body_node["value_type"]

                            if value_type == "STRING":

                                python_code += f'    print("{value}")\n'

                            elif value_type == "VARIABLE":

                                python_code += f'    print({value})\n'

                # ELSE
                if node["else"] is not None:

                    python_code += 'else:\n'

                    for body_node in node["else"]:

                        if body_node["type"] == "PRINT":

                            value = body_node["value"]

                            value_type = body_node["value_type"]

                            if value_type == "STRING":

                                python_code += f'    print("{value}")\n'

                            elif value_type == "VARIABLE":

                                python_code += f'    print({value})\n'

            # =========================
            # FOR
            # =========================

            elif node["type"] == "FOR":

                variable = node["variable"]

                start = self.generate_expression(node["start"])

                end = self.generate_expression(node["end"])

                python_code += f'for {variable} in range({start}, ({end}) + 1):\n'

                for body_node in node["body"]:

                    if body_node["type"] == "PRINT":

                        value = body_node["value"]

                        value_type = body_node["value_type"]

                        # STRING
                        if value_type == "STRING":

                            python_code += f'    print("{value}")\n'

                        # VARIÁVEL
                        elif value_type == "VARIABLE":

                            python_code += f'    print({value})\n'

        return python_code