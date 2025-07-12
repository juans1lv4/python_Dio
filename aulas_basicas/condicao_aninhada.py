conta_normal = False
conta_universitario = True


saldo = 3000
saque = 2500
cheque_especial = 500

if conta_normal:
    if saldo >= saque:
        print('saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado utilizando cheque especial')
    else:
        print('saldo insuficiente')

elif conta_universitario:
    if saldo >= saque:
        print('saque realizado com sucesso')
    else:
        print('saldo insuficiente')
        