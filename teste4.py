# Write code below 💖
import random

lista = [
    'Don t pursue happiness – create it.',
    'All things are difficult before they are easy',
    'The early bird gets the worm, but the second mouse gets the cheese.',
    'Someone in your life needs a letter from you.',
    'Dont just think. Act!',
    'Your heart will skip a beat.',
    'The fortune you search for is in another cookie.',
    'Help! Im being held prisoner in a Chinese bakery!'
]

def fortune():
    random_fortune = random.randint(0, len(lista) - 1)
    return lista[random_fortune]

print(fortune()) 
    