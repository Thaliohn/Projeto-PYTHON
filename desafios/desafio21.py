# Criar uma lista com o nome de 3 cidades, ler 'Nome Cidade', se tiver na lista imprimir 'está na lista
# Se não, não está na lista

cidades = ('Maceió', 'Aracaju', 'Teresina')
pergunta = input('Digite uma cidade\n')
if pergunta in cidades:
    print('Está na lista')
else:
    print('Não está na lista')