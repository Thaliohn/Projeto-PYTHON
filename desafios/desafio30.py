# Criar um lambda que aceite 2 números e retorne a multiplicação

multi = lambda x, y: x * y

pergunta = int(input('Digite um número: '))
pergunta1 = int(input('Digite um número: '))
print(f'A multiplicação entre os números escolhidos é: {multi(pergunta, pergunta1)}')