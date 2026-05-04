# 1. Solicite uma nota entre 0 e 10. Continue pedindo até que o usuário informe um valor válido

nota = float(input('digite a sua nota de 0 a 10: '))

while nota < 0 or nota > 10:
    print('nota invalida!')
    nota = float(input('digite a sua nota de 0 a 10: '))

else:
    print('recebemos sua nota!')