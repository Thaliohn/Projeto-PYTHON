# Crie uma lista com os carros 'BMW X6, BMW i5, BMW i8', ler o carro do usuário e se tiver em estoque imprimir "Em estoque"
# Se não, imprimir "Desculpe, carro não disponível"

carros = ['BMW X6', 'BMW i5', 'BMW i8']
carro_usuario = input("Digite o carro que você deseja: ")

if carro_usuario not in carros:
    print('Desculpe não temos este modelo disponível.')
else:
    print('Carro em estoque.')