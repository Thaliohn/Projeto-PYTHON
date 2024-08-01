# Criar uma função que calcula a potência de um número
# Dois argumentos: a base e o expoente
# Se o expoente não for fornecido colocar o número 2 como padrão

def potencia(base, expo=2):
    return base ** expo

print(potencia(3, 3))