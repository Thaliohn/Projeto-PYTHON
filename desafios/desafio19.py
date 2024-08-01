# Criar um loop para ler o nome de uma fruta, se a fruta não for 'abacate', o loop continua pedindo mais frutas
# Se for 'abacate' encerrar o loop e imprimir 'Parabéns você acertou a fruta!'

while True:
    fruta = input('Digite uma fruta: ')
    if fruta == 'abacate':

        break
    
print('Parabéns você acertou a fruta!')