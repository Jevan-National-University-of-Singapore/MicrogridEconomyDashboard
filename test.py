class Test:
    def __init__(self, var:int = 1):
        self.var = var
    
    def push(self):
        self.var += 1

test1 = Test()
test2 = Test()

test1.push()

print(test1.var)


