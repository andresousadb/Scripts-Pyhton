from time import sleep
def maior(*num):
    cont = maior = 0
    print('\033[1;34mANALISANDO MAIOR DE: \033[m ',end='')
    sleep(0.5)
    for valores in num:
        print(f'{valores} ', end='')
        if cont == 0:
            maior = valores
        else:
            if valores > maior:
                maior = valores
        cont +=1
    print(f'\nA quantidade de numeros é {cont}')
    print(f'O maior numero digitado foi {maior}')





#PROGRAMA
maior(1, 5, 9, 7, 8, 10)
maior(1, 6, 23, 96)
maior(1, 50)
maior(10)
maior()
