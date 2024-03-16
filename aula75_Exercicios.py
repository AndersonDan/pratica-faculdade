# Exercícios
# Crie funções que duplicam, multiplicam e quadriplicam
# o número recebido como parâmetro.


# def duplicar(numero):
#     return numero * 2

# def triplicar(numero):
#     return numero * 3

# def quadruplicar(numero):
#     return numero * 4


# print('Duplicar 2 =', duplicar(2))
# print('Triplicar 2 =', triplicar(2))
# print('Quadruplicar 2 =', quadruplicar(2))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print('Duplicar 2 =', duplicar(2))
print('Triplicar 2 =', triplicar(2))
print('Quadruplicar 2 =', quadruplicar(2))