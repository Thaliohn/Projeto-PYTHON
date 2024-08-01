# Criar duas funções, a primeira deve aceitar um número e retornar o dobro
# A segunda deve aceitar um número e retornar o quadrado
# Chamar a primeira dentro da segunda para retornar o quadrado do dobro

def dobro(x):
    return x * 2

def quadrado(x):
    return dobro(x) ** 2

pergunta = int(input('Digite um número: '))

print(f'O dobro do número escolhido é {dobro(pergunta)}, o quadrado do dobro é {quadrado(pergunta)}.')