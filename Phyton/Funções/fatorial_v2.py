def fatorial(n, show=True):
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
        if c > 1:
            print(' X ', end='')
        else:
            print(' = ', end='')

        f *= c
    return f


# programa
print(fatorial(2))
