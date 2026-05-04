# 2. Peça ao usuário para digitar uma senha. Continue solicitando até que ele acerte a senha correta
# (defina uma senha fixa no código)

numero = int(input(' digite a senha de quatro digitos: '))
senha = 1234

while numero != 1234:
    print('senha invalida digite a senha correta: ')
    numero = int(input('digite a senha de quatro digite: '))

else:
    print('senha correta prossiga')