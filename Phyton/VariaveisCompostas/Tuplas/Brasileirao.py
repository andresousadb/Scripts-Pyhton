times = ('Athletico-PR','Atlético-GO','Atlético-MG','Bahia','Botafogo','Bragantino','Ceará','Corinthians','Coritiba','Flamengo',
         'Fluminense','Fortaleza','Goiás','Grêmio','Internacional','Palmeiras','Santos','São Paulo','Sport','Vasco')

print('-='*30)
print(f'Lista de times do Brasileirao {times}')
print('-='*30)
print(f'Os 5 Primeiros times são {times[0:5]}')
print('-='*30)
print(f'Os 4 ultimos são {times[-4:]}')
print('-='*30)
print(f'Times em ordem alfabetica: {sorted(times)}')
print('-='*30)
print(f'O botafogo está na {times.index("Botafogo")+1} posicao')
