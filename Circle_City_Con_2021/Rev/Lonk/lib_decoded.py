class rec_num:
    def __init__(self, n=None):
        self.n = n


def number(a):
    h = rec_num()
    c = h
    while a > 0:
        c.n = rec_num()
        c = c.n
        a -= 1
    return h.n


def eval_num(a):
    i = 0
    while a:
        i += 1
        a = a.n
    return i


def copy_num(a):
    h = rec_num()
    b = h
    while a:
        b.n = rec_num()
        b = b.n
        a = a.n
    return h.n


def add(a, b): # addition
    h = copy_num(a)
    c = h
    while c.n:
        c = c.n
    c.n = copy_num(b)
    return h


def sub(a, b): # subtraction
    h = copy_num(a)
    c = h
    d = b
    while d:
        c = c.n
        d = d.n
    return c


def mult(a, b): # multiplication
    h = rec_num()
    c = a
    while c:
        h = add(h, b)
        c = c.n
    return h.n


def mod(a, b):
    r = copy_num(b)
    c = r
    while c.n:
        c = c.n
    c.n = r

    d = r
    c = a
    while c.n:
        d = d.n
        c = c.n

    if id(d.n) == id(r):
        r = None
    else:
        d.n = None

    return r


def exp(a, b):
    h = rec_num()
    c = b
    while c:
        h = mult(h, a)
        c = c.n
    return h


def mod_exp(a, b, m):
    return mod(exp(a, b), m)


def print_c(n):
    print(chr(eval_num(n)), end="", flush=True)
