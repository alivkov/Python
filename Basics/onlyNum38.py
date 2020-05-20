def foo(lst):
    return[i if not isinstance(i, str) else 0 for i in lst]

