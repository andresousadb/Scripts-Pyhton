cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    digite = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= digite <= 20:
        break
    print('Tente novamente')
print(f'Você digitou o numero {cont[digite]}')

