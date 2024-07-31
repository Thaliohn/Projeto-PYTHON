# Dicionários
 # São mutáveis

#aluno = {'nome': 'Ana', 'idade': 14, 'nota_final': 'A', 'aprovacao': True}
#del aluno[] - Remove uma key e os values dessa key
#aluno.update({'key', 'value'}) - Adiciona uma key e values
#aluno.get('exemplo', 'não existe') - Se o exemplo não existir não vai mostrar o valor aplicado

# Items, Keys e Values no Dictionary
aluno = {
        'nome': 'Ana', 
        'idade': 14, 
        'nota_final': 'A', 
        'aprovacao': True,
        'materias': ['Fisica', 'Portugues']
}

print(aluno.keys())
print(aluno.items())
print(aluno.values())