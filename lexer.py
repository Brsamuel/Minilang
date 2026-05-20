class Lexer:

    def tokenize(self, code):

        tokens = []

        lines = code.split("\n")

        for line in lines:

            line = line.strip()

            if line == "":
                continue

            parts = line.split()

            tokens.append(parts)

        return tokens