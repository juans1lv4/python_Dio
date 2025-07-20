# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input('Numero de participantes: ').strip())

# TODO: Crie um loop para armazenar participantes e seus temas:

for _ in range(n):
    entrada = input('Digite o tema e seu nome: ').strip()

    if ',' in entrada:
        participantes, tema = entrada.split(',', 1)
        participantes = participantes.strip()
        tema = tema.strip()

        if tema not in eventos:
            eventos[tema] = []
        eventos[tema].append(participantes)


# Exibe os grupos organizados
for tema, participantes in eventos.items():
    print(f"{tema}: {', '.join(participantes)}")