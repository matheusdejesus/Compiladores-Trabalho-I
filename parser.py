class Parser:
    def __init__(self, input_string):
        self.input_string = input_string
        self.tokens = [c for c in input_string if c != ' ']
        self.pos = 0

    def current(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def match(self, expected):
        if self.current() == expected:
            self.pos += 1
        else:
            raise Exception(f"\033[31mErro\033[0m de sintaxe na coluna {self.pos + 1}: "
                          + f"esperado '{expected}', encontrado '{self.current()}'")

    def parse(self):
        try:
            self.BOOL()
            if self.pos != len(self.tokens):
                raise Exception(f"\033[31mErro\033[0m: Entrada "
                              + "restante não consumida a partir "
                              + f"do index {self.pos + 1}")
            print(f"Entrada '{self.input_string}': \033[32mAceita\033[0m!")
        except Exception as e:
            print(f"Entrada '{self.input_string}': \033[31mRejeitada\033[0m! {e}")

    def BOOL(self):
        self.JOIN()
        while self.current() == '|':
            self.match('|')
            self.JOIN()

    def JOIN(self):
        self.EQUAL()
        while self.current() == '&':
            self.match('&')
            self.EQUAL()

    def EQUAL(self):
        self.REL()
        while self.current() in ['=', '~']:
            self.match(self.current())
            self.REL()

    def REL(self):
        self.EXPR()
        while self.current() in ['<', '>']:
            self.match(self.current())
            self.EXPR()

    def EXPR(self):
        self.TERM()
        while self.current() in ['+', '-']:
            self.match(self.current())
            self.TERM()

    def TERM(self):
        self.UNARY()
        while self.current() in ['*', '/']:
            self.match(self.current())
            self.UNARY()

    def UNARY(self):
        if self.current() in ['!', '-', '+']:
            self.match(self.current())
            self.UNARY()
        else:
            self.FACTOR()

    def FACTOR(self):
        if self.current() == '(':
            self.match('(')
            self.BOOL()
            self.match(')')
        elif (self.current() in ['a', 'b', 'c', 't', 'f']
              or (self.current()
                  and self.current().isdigit())
              ):
            self.match(self.current())
        else:
            raise Exception(f"Erro de sintaxe no fator na coluna "
                          + f"{self.pos + 1}: token inválido "
                          + f"'{self.current()}'")


if __name__ == "__main__":
    exemplos = ["a|b", "!(a=b)&f", "(a+b)>fdfc"]
    for string in exemplos:
        parser = Parser(string)
        parser.parse()