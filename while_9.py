# 9. Peça números ao usuário até que ele digite 0. Ao final, informe quantos números positivos e quantos
# negativos foram digitados
positivo = 0
negativo = 0
numero = -1

while numero != 0:
    numero = int(input('digite um numero positivo ou negativo: '))
    if numero > 0:
        positivo = positivo + 1
    elif numero < 0:
        negativo = negativo + 1
print(f'a quantidade de numeros positivos é: {positivo}')
print(f'a quantidade de numerod negativos é: {negativo}')