# Criar uma função lambda que eleve um número ao quadrado
# Depois usar a função para calcular o quadrado de todos os números em uma lista usando for

lista = [2,3,6,8,9]

sqrt = lambda x: x ** 2

result = []

for num in lista:
    result.append(sqrt(num))
    
print(f'O resultado é {result}')