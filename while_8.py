# 8. Peça um número e mostre a tabuada dele de 1 a 10

n = int(input('digite um numero: '))
while n >= 0:
    n1 = n * 1
    n2 = n * 2
    n3 = n * 3
    n4 = n * 4
    n5 = n * 5
    n6 = n * 6
    n7 = n * 7
    n8 = n * 8
    n9 = n * 9
    n10 = n * 10
    print (n1, n2, n3, n4, n5, n6, n7, n8, n9, n10)
    break

# SEGUNDA FORMA

numero = int(input("Digite um número para ver a tabuada: "))

# Iniciamos o multiplicador em 1
i = 1

print(f"Tabuada do {numero}:")

# O loop vai rodar de 1 até 10
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    
    # Incrementamos o i para passar para o próximo número da tabuada
    i = i + 1