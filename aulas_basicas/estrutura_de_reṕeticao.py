#usar o for quando sabemos a quantidade de vezes que o numero sera repetido
notas = {
    'Portugues': 7,
    'Matematica': 9.0,
    'Logica': 10
}

for chave, valor in notas.items():
    print(f'{chave}: {valor}')
    if valor == 10:
        print(f'Parabens sua nota em {chave} foi {valor}')
