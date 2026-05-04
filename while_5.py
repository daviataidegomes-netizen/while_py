# 5. Peça números ao usuário continuamente e informe se cada número é par ou ímpar. O programa só
# deve parar quando o usuário digitar 0

numero = int(input('digite um numero: '))
saída = 0
while numero != saída:
    if numero == 0:
        print('programa errado')
    elif numero % 2 == 0:
        print(numero, 'é par')
    else:
        print(numero, 'é impar')
    break

# SEGUNDA FORMA:

numero = -1
saída = 0
while numero != saída:
    numero = int(input('digite um numero: '))
    if numero == saída:
        print('você digitou o codigo para sair')
    elif numero % 2 == 0:
        print('o numero', numero, 'é par')
    else:
        print('o numero', numero, 'é impar')

    
    




