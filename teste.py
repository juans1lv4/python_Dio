Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print('Q1) Do you like Dawn or Dusk?\n'
        '1) Dawn\n'
        '2) Dusk')
resposta = int(input('Qual sua resposta:'))

if resposta == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif resposta == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print('informação errada!')

print('---------------------')
print('Q2) When I’m dead, I want people to remember me as:\n'
        '1) The Good\n'
        '2) The Great\n' 
        '3) The Wise\n' 
        '4) The Bold')
resposta2 = int(input('Qual sua resposta:'))

if resposta2 == 1:
    Hufflepuff += 2
elif resposta2 == 2:
    Slytherin += 2
elif resposta2 == 3:
    Ravenclaw += 2
elif resposta2 == 4:
    Gryffindor += 2
else:
    print('informação errada!')
print('---------------------')

print('Q3) Which kind of instrument most pleases your ear?\n'
    '1) The violin\n'
    '2) The trumpet\n'
    '3) The piano\n'
    '4) The drum')
resposta3 = int(input('Qual sua resposta:'))

if resposta3 == 1:
     Slytherin += 4
elif resposta3 == 2:
    Hufflepuff += 4
elif resposta3 == 3:
    Ravenclaw += 4
elif resposta3 == 4:
    Gryffindor += 4
else:
    print('informação errada!')
print('---------------------')

print(f'A pontuação de Gryffindor é: {Gryffindor}')
print(f'A pontuação de Ravenclaw é: {Ravenclaw}')
print(f'A pontuação de Hufflepuff é: {Hufflepuff}')
print(f'A pontuação de Slytherin é: {Slytherin}')