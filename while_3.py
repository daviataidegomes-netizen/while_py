# 3. Peça um número inteiro positivo N e mostre todos os números de 1 até N usando repetição

i = 0
n = int(input('digite um numero inteiro positivo'))

while n >= i:
    print(n)
    n = n - 1

else:
    print('numero não positivo')