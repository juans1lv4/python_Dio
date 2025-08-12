import textwrap

def menu(): 
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nc] Nova Conta
    [lc] Listar contas
    [nu] Novo usuario
    [q] Sair
    ==> """
    return input(textwrap.dedent(menu))



def depositar(saldo, valor, extrato, /):
        if valor > 0:
            saldo += valor
            extrato += f'Deposito: R$ {valor:.2f}\n'
            print('Deposito realizado com sucesso')
        else:
            print('Erro de operação, informe um valor valido.')
        return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, num_saque, LIMITE_SAQUE):
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

        return saldo, extrato, num_saque

def exibir_extrato(saldo, /, *, extrato):
        print('\n===== EXTRATO =====')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        #print(f'\nSaques realizados no dia: {num_saque}')
        print('\n===============')

def criar_usuario(usuarios):
    cpf = input('Informe o CPF: ')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
         print('Já existe usuario com esse cpf')
         return
    
    nome = input('informe seu nome')
    data_nasc = input('sua data de nascimento')
    endereco = input('informe seu enderço')

    usuarios.append({'nome': nome, 'data_nasc': data_nasc, 'cpf': cpf, 'endereco': endereco})
    print('=== usuario criado com sucesso ===')

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrado = [usuario for usuario in usuarios if usuario['cpf']==cpf]
    return usuarios_filtrado[0] if usuarios_filtrado else None

def criar_conta(agencia, num_conta, usuarios):
    cpf = input('Informe o cpf do usuario')
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
         print("\n=== Conta criada com sucesso! ===")
         return {'agencia': agencia, 'numero_conta': num_conta, 'usuarios': usuario}
    print('Usuário não encontrado, fluxo de criação de conta encerrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuarios']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))



def main():

    saldo = 0
    limite = 500
    extrato = ''
    num_saque = 0
    LIMITE_SAQUE = 3
    AGENCIA = '0001'
    usuarios = []
    contas = []


    while True:
         opcao = menu()

         if opcao == 'd':
              valor = float(input('Informe o valor do déposito: '))
              saldo, extrato = depositar(saldo, valor, extrato)
         elif opcao == 's':
              valor = float(input('Informe o valor do saque: '))
              saldo, extrato, num_saque = sacar(
                   saldo=saldo,
                   valor=valor,
                   extrato=extrato,
                   limite=limite,
                   num_saque=num_saque,
                   LIMITE_SAQUE=LIMITE_SAQUE,
              )

         elif opcao == 'e':
              exibir_extrato(saldo, extrato=extrato)
         elif opcao == 'nu':
              criar_usuario(usuarios)
         elif opcao == 'nc':
              numero_conta = len(contas) + 1
              conta = criar_conta(AGENCIA, numero_conta, usuarios)

              if conta:
                   contas.append(conta)

         elif opcao == 'lc':
              listar_contas(contas)
         elif opcao == 'q':
              break

         else:
              print("Operação inválida, por favor selecione novamente a operação desejada.")


main()