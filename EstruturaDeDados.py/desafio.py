# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input('Quantos itens foi adicionado no carrinho? ').strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input('Adicionar itens:').strip()
    
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    
    # Adiciona ao carrinho
    carrinho.append((item, preco))
    total += preco

for item, preco in carrinho:
    print(f'{item}: R$ {preco:.2f}')
print(f'total: R$ {total:.2f}')

# TODO: Exiba os itens e o total da compra