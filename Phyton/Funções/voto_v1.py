def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 18:
        return f'Com {idade} de idade:NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} de idade: VOTO OPICIONAL'
    else:
        return f''




#programa principal
nasc = int(input('Em que ano você nasceu: '))
print((voto(nasc)))