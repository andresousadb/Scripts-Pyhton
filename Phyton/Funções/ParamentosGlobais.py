def teste(b):
    global a
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'b dentro vale {b}')
    print(f'c dentro vale {c}')

#PROGRAMA
a = 5
teste(a)
print(f'A fora vale {a}')