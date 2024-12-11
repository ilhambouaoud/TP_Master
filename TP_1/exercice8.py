def somme_varargs(*args):
    s = 0
    for i in args: s += i
    return s



print(somme_varargs(90,76,34,29))
