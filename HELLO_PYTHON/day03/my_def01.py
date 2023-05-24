def add(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return int(a / b)


def namuji(a, b):
    return a % b


sum = add(4, 3)  # @ReservedAssignment
min = minus(4, 3)  # @ReservedAssignment
mul = multiply(3, 2)
div = divide(4, 3)
mod = namuji(4, 3)
print(sum)
print(min)
print(mul)
print(div)
print(mod)
