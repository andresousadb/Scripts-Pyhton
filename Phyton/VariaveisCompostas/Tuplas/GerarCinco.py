from random import randint
num = (randint(1,10), randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('O valores sorteados foram:',end=' ')
for c in num:
    print(f'{c}',end=' ')
print(f'\n\033[1;33m O maior numero sorteado foi {max(num)}\033[m')
print(f'\033[1;30m O menor numero sorteado foi {min(num)}')
