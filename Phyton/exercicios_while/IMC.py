peso = int(input('Qual o seu peso? (kg) '))
altura = float(input('Qual a sua altura? (m) '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Você está abaixo do Peso minimo')
elif 18.5 <= imc < 25:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('PARABENS, você está na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('Cuidado! você está com Sobrepeso')
elif 30 <= imc < 40:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('ATENÇÃO ! você está com obesidade')
else:
    print('O IMC dessa pessoa é de {:.1f}'.format(imc))
    print('ATENÇÃO ! CUIDADO ! você está com obesidade Mórbida')
