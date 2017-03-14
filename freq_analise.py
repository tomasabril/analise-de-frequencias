##


frase = input("Digite a frase para analisar: \n")

frequencias = {}

for letra in frase:
    if letra not in frequencias:
        frequencias[letra] = 1
    else
        frequencias[letra] += 1
print(frequencias)