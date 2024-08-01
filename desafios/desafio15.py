# Criar uma lista de frutas e colocar maçã 3 vezes e outras frutas
# Usar um loop pra contar quantas vezes maçã aparece na lista

frutas = ['maçã','maçã','maçã','manga','uva','banana']
contador = 0

for fruta in frutas:
    if fruta == 'maçã':
        contador += 1

print(contador)