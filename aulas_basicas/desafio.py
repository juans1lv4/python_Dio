# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input('Digite o valor: ').strip())
cupom = input('Digite seu cupom: ').strip()



if cupom in descontos:
    desconto = descontos[cupom]
    print('Cupom ativiado com sucesso')
    preco_final = preco * (1 - desconto)
    print(f"Valor final com desconto: {preco_final:.2f}")

else:
    preco_final = preco
    print('Digite um cupom valido')
    print(f"{preco_final:.2f}")



# TODO: Aplique o desconto se o cupom for válido: