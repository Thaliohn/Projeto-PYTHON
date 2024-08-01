# Criar uma função lambda que aceita um número e retorna o cubo do número

cubo = lambda cube: cube ** 3

pergunta = int(input('Digite um número: '))
print(f'O cubo do número {pergunta} é {cubo(pergunta)}')