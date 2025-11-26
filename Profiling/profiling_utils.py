
def calc_triples(max_):
    triples = []
    for a in range(1, max_ + 1):
        for b in range(a, max_ + 1):
            hypotenuse = calc_hypotenuse(a, b)
            if is_int(hypotenuse):
                triples.append((a, b, int(hypotenuse)))
    return triples


def calc_triples_faster(max_):
    triples = []
    for a in range(1, max_ + 1):
        for b in range(a, max_ +1):
            hypotenuse = (a*a + b*b) ** 0.5
            if hypotenuse.is_integer():
                triples.append((a, b, int(hypotenuse)))
    return triples


def calc_triples_generator(max_):
    # triples = []
    for a in range(1, max_ + 1):
        for b in range(a, max_ +1):
            hypotenuse = (a*a + b*b) ** 0.5
            if hypotenuse.is_integer():
                yield a, b, int(hypotenuse)



def calc_hypotenuse(a, b):
    return (a*a + b*b) ** 0.5


def is_int(n):
    return n.is_integer()


