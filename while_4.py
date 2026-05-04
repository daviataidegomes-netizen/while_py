# 4. Peça números ao usuário e some-os. O programa deve parar quando o usuário digitar um número
# negativo. Ao final, mostre a soma total

n1 = int(input('digite um valor para n1: '))
n2 = int(input('digite um valor para n2: '))

i = 0
while i == 0:
    if n1 > i and n2 > i:
        soma = n1 + n2 
        print(soma)
        break
    else:
        print('digite um numero positivo')
        break


soma = 0 # essa é no caixa vazia, colocamos a 0 pois não sabemos nem recebemos nenhum outro valor
numero = 0 # deixamos maior ou igual a zero para esse numero possa entrar no while

# O loop continua enquanto o número digitado for positivo ou zero
while numero >= 0:
    numero = float(input("Digite um número para somar (ou negativo para sair): "))
    
    # Sem esse if, se você somasse 10 + 10 e digitasse -1 para sair, o resultado final seria 19
    if numero >= 0:     # if garante que a soma ocorra caso o "numero" seja atendido
        soma = soma + numero

print("A soma total é:", soma)