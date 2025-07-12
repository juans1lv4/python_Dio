# utilizar quando nao sabemos por quanto tempo precisa se reprtir o loop, ao contrario do for
# So sera utilizado quando a condição for verdadeira
'''opcao = -1

while opcao != 11:
    opcao = int(input('[1] sacar \n[2] extrato \n[0] sair \n:'))

    if opcao == 1:
        print('sacando....')
    elif opcao == 2:
        print('exibindo extrato......')

else:
    print('fechando loop')
    '''

contador = 0

while contador < 10:
    ##print(f'Valor do contador é {contador}')
    contador += 1
    if contador != 3:
        print(f'Valor do contador é {contador}')
    elif contador == 3:
        print(f'estou no contador {contador}')
