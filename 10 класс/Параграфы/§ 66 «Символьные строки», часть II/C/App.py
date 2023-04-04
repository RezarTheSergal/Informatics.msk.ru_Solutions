class Replacer:
    def __init__(self, s):
        self.s = s
        self.pos_b = 0
        self.pos_r = 0

    def replace(self):
        result = self.replace_r()
        return result

    def replace_r(self):
        self.pos_r = self.s.find('R')
        self.s = self.s[:self.pos_r] + self.s[self.pos_r:].replace('R', '', 1)
        return self.replace_b()

    def replace_b(self):
        self.pos_r = self.s.rfind('B')
        self.s = self.s[:self.pos_r] + self.s[self.pos_r:].replace('B', '', 1)
        return self.replace_r() if self.check() else self.s

    def check(self):
        c = 0
        for i in range(1, len(self.s)):
            if self.s[i-1] != self.s[i]:
                c += 1
        if c > 1:
            return True
        else:
            return False

a = input()
replacer = Replacer(a)
result = replacer.replace()
print(result)
print(len(a) - len(result))
