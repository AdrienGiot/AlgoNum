# root search - Felix
def root(f, a, b, h):
    """
        f = funct
        a = first born
        b = last born
        h = number of steps
    """
    parser = a
    step = (b - a)/h
    while parser <= b:
        f_parser = f(parser)
        f_parser_step = f(parser + step)
        if f_parser == 0:
            return parser
        if f_parser_step == 0:
            return parser + step
        if (f_parser < 0 and f_parser_step > 0) or (f_parser > 0 and f_parser_step < 0):
            return (parser, parser + step)
        parser += step
    return None

if __name__ == "__main__":
    f = lambda x : 3*x -3
    print(root(f, -5, 5, 1000))
    print(root(lambda x : 1, -5, 5, 1000))