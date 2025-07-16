numero = {1, 1, 3, 5, 6}
print(numero)

print('-----------------')

numero = list(numero)
print(numero)

print('-----------------')

conjuntA = {4, 4, 7, 3, 10}
conjuntB = {10, 4, 90, 100}

uniao = conjuntA.union(conjuntB)
print(uniao)

print('-----------------')

inter = conjuntA.intersection(conjuntB)
print(inter)

print('-----------------')

difreA = conjuntA.difference(conjuntB)
difreB = conjuntB.difference(conjuntA)
print(difreA)
print(difreB)

print('-----------------')

symmetric = conjuntA.symmetric_difference(conjuntB)
print(symmetric)

a = int(input('Digte um numero:'))
b = int(input('Digte um numero:'))

result =  (a ** 2 + b ** 2)**2

print(result)