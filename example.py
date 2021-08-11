def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError('dividir() deve apena receber argumentos inteiros')
    try:
        aux = dividendo / divisor
    except:
        print(f'Não foi possivel dividir {dividendo} por {divisor}')
        raise
    return aux


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f'O resultado da divisão de 10 por {divisor} é {resultado}')


# try:
#     testa_divisao(2.5)
#
# except ZeroDivisionError as E:
#     print('Erro de divisão por zero')
#
# #except Exception as E:
# #    print('Tratamento generico')
#
# print('Programa encerrado')

try:
    print('O fluxo esta aqui')
    raise ValueError
except Exception:
    print('Agora ele veio para cá')

print('E enfim ele contiua...')