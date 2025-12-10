class Counter():
    def __init__(self, initial_count):
        self.inital_count = initial_count

    def increment(self):
        self.inital_count += 1
    
    def get(self):
        return self.inital_count

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)