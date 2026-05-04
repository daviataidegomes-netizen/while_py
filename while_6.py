# 6. Peça vários números ao usuário (encerra com 0) e informe qual foi o maior número digitado

base = 0
n1 = float(input('digite um numero: '))
n2 = float(input('digite um numero: '))

while n1 > 0 and n2 > 0:
    if n1 > n2:
        print(n1)
        print(n2)
    else:
        print(n2)
        print(n1)
    break
else:
    print('um de seus numeros não é maior que 0!')


# SEGUNDA FORMA:

# Inicializamos com um valor bem pequeno para que qualquer número digitado ganhe dele
maior = 0         # imaginar 0 como um valor a ser batido, quando colocamos 
numero = -1

while numero != 0:
    numero = int(input("Digite um número (ou 0 para parar): "))
    
    # Se o número atual for maior que o nosso 'campeão', atualizamos
    if numero > maior:       # Quando colocamos 5 o valor entendi que "maior é 5", se maior = 3
        maior = numero       # e digitarmos 2 o maior continua sendo a variavel

print(f"O maior número digitado foi: {maior}")





