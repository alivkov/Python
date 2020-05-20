def foo(lst):
    return[i for i in lst if not isinstance(i, str)]
