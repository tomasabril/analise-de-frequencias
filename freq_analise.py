##


frase = input("Digite a frase para analisar: \n")

frequencias = {}
total = 0

for letra in frase:
    if letra.isalpha() or letra.isdigit():
        if letra not in frequencias:
            frequencias[letra] = 1
        else:
            frequencias[letra] += 1
        total += 1

print(frequencias)

for i in frequencias:
    frequencias[i] /= total

print(frequencias)
