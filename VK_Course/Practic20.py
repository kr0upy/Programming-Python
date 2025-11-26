def f():
    global a
    a += 10
    return a
a = int(input())
f()
print(a)