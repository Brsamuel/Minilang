class Generator:

    def generate(self, ast):

        python_code = ""

        for node in ast:

            # PRINT
            if node["type"] == "PRINT":

                value = node["value"]

                value_type = node["value_type"]

                # STRING
                if value_type == "STRING":

                    python_code += f'print("{value}")\n'

                # VARIÁVEL
                elif value_type == "VARIABLE":

                    python_code += f'print({value})\n'

            # LET
            elif node["type"] == "LET":

                name = node["name"]

                value = node["value"]

                # NÚMERO
                if value.isdigit():

                    python_code += f'{name} = {value}\n'

                # STRING
                else:

                    python_code += f'{name} = "{value}"\n'

            # IF
            elif node["type"] == "IF":

                left = node["left"]

                operator = node["operator"]

                right = node["right"]

                python_code += f'if {left} {operator} {right}:\n'

                for body_node in node["body"]:

                    # PRINT dentro do IF
                    if body_node["type"] == "PRINT":

                        value = body_node["value"]

                        value_type = body_node["value_type"]

                        # STRING
                        if value_type == "STRING":

                            python_code += f'    print("{value}")\n'

                        # VARIÁVEL
                        elif value_type == "VARIABLE":

                            python_code += f'    print({value})\n'

            # FOR
            elif node["type"] == "FOR":

                variable = node["variable"]

                start = node["start"]

                end = int(node["end"]) + 1

                python_code += f'for {variable} in range({start}, {end}):\n'

                for body_node in node["body"]:

                    # PRINT dentro do FOR
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