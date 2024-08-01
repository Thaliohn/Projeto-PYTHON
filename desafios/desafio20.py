# Criar uma lista de 1 a 10 e usar um for loop para iterar a lista, se o numero for par imprimir 'par'
# Se for impar imprimir 'impar'

lista = [1,2,3,4,5,6,7,8,9,10]
for numero in lista:
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é impar')