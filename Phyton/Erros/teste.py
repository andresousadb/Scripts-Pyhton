try:
    a = int(input('Numeroador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError,TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou. ')
except ZeroDivisionError:
    print('Não é possivel dividir um numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')
except Exception as erro:
    print(f'O erro encontrato foi {erro.__class__}')
else:
    print(f'O Resultado é {r:.1f}')
finally:
    print('Volte sempre !!')
