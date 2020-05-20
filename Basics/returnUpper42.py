def foo(*args):
    for i in args:
        return str.upper(i)

print(foo("dog", "cat", "bird"))
