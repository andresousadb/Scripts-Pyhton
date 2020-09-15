# def linhas():
#     print('-='*20)
#
#
# linhas()
# print('CADASTRO CLIENTES')
# linhas()
# print('FUTEBOL')
# linhas()
# print('LOTERICA')
# linhas()

# def mensagem(msg):
#     print('-' * 30)
#     print(msg)
#     print('-' * 30)
#
#
# mensagem('      SISTEMA DE ALUNO    ')
# mensagem('          CADASTRO        ')
# mensagem('      CURSO EM VIDEO      ')

print('     RESULTADO       ')


def soma(* valores):
    s = 0
    for num in valores:
        s +=num
    print(f'O RESULTADO DA SOMA DE {valores} temos {s}: ')


#PROGRAMA DE SOMA
soma(7, 5)
soma(8, 9)
soma(2, 1, 10)

# def contador(*num):
#     s = len(num)
#     print(f'Recebi os valores {num} que tem a quantidade de {s}')
#
#
# contador(1, 8, 9)
# contador(8, 9, 10)
# contador(9, 10, 11, 15)

# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] *=2
#         pos += 1
#
#
# valores = [6, 8, 9, 5, 4]
# dobra(valores)
# print(valores)

