# Lambda Function
 # É uma função pequena
 # Geralmente usada dentro de outras funções

'''somar10 = lambda x, y: x + y + 10
print(somar10(3, 6))'''

# Lambda dentro de uma função
'''def somar(x):
    var = lambda x: x + 10
    return var(x) * 4

print(somar(5))'''

# Função map()
'''lista_um = [1, 4, 8, 3]
def multi(x):
    return x * 3

lista_dois = map(multi, lista_um)
print(list(lista_dois))'''

# Função map associada a lambda
'''lista = [1, 4, 6, 7]
lista2 = map(lambda x: x * 2, lista)
print(list(lista2))
# Ou
print(list(map(lambda x: x * 2, lista)))'''

# Função Filter
'''valores = [33, 44, 102, 250]
def filtrar_menos_de_50(x):
    return x > 50

print(list(filter(filtrar_menos_de_50, valores)))
print(list(filter(lambda x: x > 50, valores)))'''

# List Comprehension
'''nomes = ['Carlos', 'Juan', 'Maria', 'Kayllane']
x = []
for nome in nomes:
    if 'e' in nome:
        x.append(nome)
# Jeito rápido
print(x)
x = [nome for nome in nomes if 'i' in nome]
print(x)'''

# List Comprehension com Números, o list comprehension utiliza a fórmula [expressão for item in item]
'''numeros = [x * 3 for x in range(6)]
print(numeros)'''

# Generator e diminuir tamanho de programas
'''from sys import getsizeof as gso
valores = [x * 5 for x in range(6)]
print(gso(valores))
#############################################
valores = (x * 5 for x in range(6))
print(gso(valores))
'''

