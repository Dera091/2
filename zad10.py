import math
class kwadrat:
    def __init__(self, a):
        self.a = a

    def obwód(self):
        return self.a * 4
    
    def pole(self):
        return self.a * self.a
class prostokąt:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def obwód(self):
        return self.a * 2 + self.b * 2
    
    def pole(self):
        return self.a * self.b   
class trójkątrównoboczny:
    def __init__(self, a):
        self.a = a
        
    def obwód(self):
        return self.a * 3
    
    def pole(self):
        return self.a * self.a * math.sqrt(3) / 4

k = kwadrat(3)
p = prostokąt(3, 4)
t = trójkątrównoboczny(5)

print(k.obwód())
print(k.pole())

print(p.obwód())
print(p.pole())

print(t.obwód())
print(t.pole())