class Parser:

    def parse(self, tokens):

        ast = []

        i = 0

        while i < len(tokens):

            line = tokens[i]

            command = line[0]

            # PRINT
            if command == "PRINT":

                raw_value = " ".join(line[1:])

                # STRING
                if '"' in raw_value:

                    value = raw_value.replace('"', '')

                    ast.append({
                        "type": "PRINT",
                        "value": value,
                        "value_type": "STRING"
                    })

                # VARIÁVEL
                else:

                    ast.append({
                        "type": "PRINT",
                        "value": raw_value,
                        "value_type": "VARIABLE"
                    })

            # LET
            elif command == "LET":

                variable_name = line[1]

                value = " ".join(line[3:])

                value = value.replace('"', '')

                ast.append({
                    "type": "LET",
                    "name": variable_name,
                    "value": value
                })

            # IF
            elif command == "IF":

                left = line[1]

                operator = line[2]

                right = line[3]

                body = []

                i += 1

                while tokens[i][0] != "END":

                    inner_line = tokens[i]

                    inner_command = inner_line[0]

                    # PRINT dentro do IF
                    if inner_command == "PRINT":

                        raw_value = " ".join(inner_line[1:])

                        # STRING
                        if '"' in raw_value:

                            value = raw_value.replace('"', '')

                            body.append({
                                "type": "PRINT",
                                "value": value,
                                "value_type": "STRING"
                            })

                        # VARIÁVEL
                        else:

                            body.append({
                                "type": "PRINT",
                                "value": raw_value,
                                "value_type": "VARIABLE"
                            })

                    i += 1

                ast.append({
                    "type": "IF",
                    "left": left,
                    "operator": operator,
                    "right": right,
                    "body": body
                })

            # FOR
            elif command == "FOR":

                variable = line[1]

                start = line[3]

                end = line[5]

                body = []

                i += 1

                while tokens[i][0] != "END":

                    inner_line = tokens[i]

                    inner_command = inner_line[0]

                    # PRINT dentro do FOR
                    if inner_command == "PRINT":

                        raw_value = " ".join(inner_line[1:])

                        # STRING
                        if '"' in raw_value:

                            value = raw_value.replace('"', '')

                            body.append({
                                "type": "PRINT",
                                "value": value,
                                "value_type": "STRING"
                            })

                        # VARIÁVEL
                        else:

                            body.append({
                                "type": "PRINT",
                                "value": raw_value,
                                "value_type": "VARIABLE"
                            })

                    i += 1

                ast.append({
                    "type": "FOR",
                    "variable": variable,
                    "start": start,
                    "end": end,
                    "body": body
                })

            i += 1

        return ast