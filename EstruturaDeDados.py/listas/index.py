frutas = ['Maça', 'Banana', 'Abacate']

print(frutas[0])

print('----------')

matriz = [
    [1, 'a', 3],
    [8, 'y', 6],
    [4, 'x', 2],
]

print(matriz[2][0])
print(matriz[1][1])
print(matriz[0][2]) 

print('----------')

carros = ['gol', 'celta', 'ferrare']

for carro in carros:
    print(carro)

print('----------')

carros = ['gol', 'celta', 'Hb20']

for indice, carro in enumerate(carros):
    print(f'{indice}: {carros[2]}')

print('----------')

numeros = [1, 4, 16, 19, 39]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(f'Numeros pares: {pares}')

quadrado = []
for numero in numeros:
    quadrado.append(numero ** 2)
print(f'Numeros elevado ao quadrado: {quadrado}')

numeroo =  [n**2 if n > 6 else n for n in range(10) if n % 2 == 0] 
print(numeroo)