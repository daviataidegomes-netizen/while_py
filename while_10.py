# 10. Defina um número fixo no código. Peça ao usuário para adivinhar até acertar. Informe se o palpite é
# maior ou menor que o número correto

codigo = 1234
senha = int(input('digite o codigo em numeros: '))

while senha != codigo:
    if senha > codigo:
        print('seu palpite é um pouco maior')
        senha = int(input('digite o codigo em numeros: '))
    else:
        print('seu palpite é um pouco menor')
        senha = int(input('digite o codigo em numeros: '))
else:
    print('seu palpite esta correto! a senha é', codigo)


