menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==> """

saldo = 0
limite = 500
extrato = ''
num_saque = 0
LIMITE_SAQUE = 3


while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Informe o valor que deseja depositar:'))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
            print('Deposito realizado com sucesso')

        else:
            print('Erro de operação, informe um valor valido.')

    elif opcao == 's':
        valor = float(input('Informe o valor que deseja sacar:'))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite

        excedeu_saques = num_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print('Operação falhou! Voce não tem saldo suficiente.')
        elif excedeu_limite:
            print('Operação falhou! Voce não tem limite suficiente, tente sacar um valor menor')
        elif excedeu_saques:
            print('Operação falhou! Voce já utulizo todo seu limite diario')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n' # esse extrato foi utuliazdo apenas para exibir os resultados de 'valor', tanto no saque quanto no deposito
            num_saque += 1
            print('Saque realizado com sucesso')

        else:
            print('Erro de operação, informe um valor valido.')

    elif opcao == 'e':
        print('\n===== EXTRATO =====')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print(f'\nSaques realizados no dia: {num_saque}')
        print('\n===============')
    elif opcao == 'q':
        print('Sistema encerrado')
        break

    else:
        print('Escolha uma opção valida')