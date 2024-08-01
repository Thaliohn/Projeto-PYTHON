# Crie uma lista de frutas e uma de vegetais e use for loop para imprimir todas as combinações possíveis

frutas = ['manga', 'maçã', 'banana', 'mamão']
vegetais = ['cebola', 'pepino', 'pimentão', 'alho']

for fruta in frutas:
    for vegetal in vegetais:
        print(f'A fruta é {fruta}, o vegetal é {vegetal}')