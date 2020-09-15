cont = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
        'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero <= 0 and numero <=20:
        break
    print('Não existe esse numero.Digite de novo ')
print(f'O numero digitado foi {cont[numero]}')
