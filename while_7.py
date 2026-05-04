# 7. Peça várias notas ao usuário (encerra quando digitar -1) e calcule a média das notas válidas

n1 = int(input('digite uma nota: '))
n2 = int(input('digite uma nota: '))
n3 = int(input('digite uma nota: '))

trava = -1
while n1 == trava or n2 == trava or n3 == trava:
    print('nota errada!')
    n1 = int(input('digite uma nota: '))
    n2 = int(input('digite uma nota: '))
    n3 = int(input('digite uma nota: '))
else:
    média = (n1 + n2 + n3) / 3
    print(média)


# SEGUNDA FORMA

soma = 0
quantidade = 0
nota = 0

while nota != -1:
    nota = float(input("Digite uma nota (ou -1 para encerrar): "))
    
    if nota != -1:
        soma = soma + nota          # Acumula o valor da nota
        quantidade = quantidade + 1  # Conta que mais uma nota foi inserida

if quantidade > 0:
    media = soma / quantidade
    print(f"Você digitou {quantidade} notas.")
    print(f"A média das notas é: {media:.2f}")
else:
    print("Nenhuma nota válida foi digitada.")


