def somar(a,b):
    return a + b

def exbir_result(a, b, funcao):
    result = funcao(a,b)
    print(f'{a} + {b} = {result}')

exbir_result(10,10, somar)