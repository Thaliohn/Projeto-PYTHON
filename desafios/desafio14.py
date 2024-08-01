# Criar um loop que imprima números de 1 a 10 mas pare de imprimir assim que chegar no 5
# Criar um segundo loop que imprima de 1 a 10 mas pule a impressão do 5

numeros = [1,2,3,4,5,6,7,8,9,10]

for numero in numeros:
   print(numero)
   if numero == 5:

    break

print('-------------')

for numero in numeros:
  print(numero)
  if numero == 4:
    numeros.remove(5)

    continue 