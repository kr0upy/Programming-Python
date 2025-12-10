class Pendulum:
    g = 10
    pi = 3.14

    @classmethod
    def calculate_period(cls, lenght):
        return (2 * cls.pi) * ((lenght / cls.g) ** 0.5)

code = []
while data := input():
   code.append(data)
code = "\n".join(code)
exec(code)
