class Parser:
    def __init__(self, s):
        self.s = s
        self.pos = 0

    def parse(self):
        result = self.parse_expression()
        return result

    def parse_expression(self):
        result = self.parse_term()
        while self.pos < len(self.s) and self.s[self.pos] in ('+', '-'):
            op = self.s[self.pos]
            self.pos += 1
            right = self.parse_term()
            result = int(result) + int(right) if op == '+' else int(result) - int(right) 
        return result

    def parse_term(self):
        result = self.parse_factor()
        while self.pos < len(self.s) and self.s[self.pos] in ('*', '/'):
            op = self.s[self.pos]
            self.pos += 1
            right = self.parse_factor()
            result = int(result) * int(right)  if op == '*' else int(result) / int(right) 
        return result

    def parse_factor(self):
        if self.s[self.pos] == '(':
            self.pos += 1
            result = self.parse_expression()
            self.pos += 1
            return result
        start_pos = self.pos
        while self.pos < len(self.s) and self.s[self.pos].isdigit():
            self.pos += 1
        return int(self.s[start_pos:self.pos])

s = input()
parser = Parser(s)
result = parser.parse()
print(result)
