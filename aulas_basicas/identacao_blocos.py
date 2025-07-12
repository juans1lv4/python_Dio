#respeitar os blocos, iniciar o bloco com :, sempre contar os 4 espaços.

def sacar(valor):
    saldo = 200

    if saldo >= valor:
        print('valor sacado com sucesso!')
    else:
        print('valor indisponivel!')

    print('obrigado por ser nosso cliente')

sacar(300)