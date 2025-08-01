#kwargs recebe um dicionario
#args é lista

def exibir_poema(data_extenso, *args, **kwargs):
    texto = '\n'.join(args)
    meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
    msg = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
    print(msg)
exibir_poema('quinta, 31 de agosto de 2025','zen of python', 'beautiful is better than ugly', autor='tim peters', ano=1999)