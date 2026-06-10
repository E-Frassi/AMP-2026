soma = 0
cont = 0
n = int(input("informe um numero:"))
while cont < n:
    valor = int(input("digite um numero:"))
    soma += valor
    cont += 1 
media = soma/n
print("soma dos numeros:")
print("quantidade de numeros digitados:", n)
print("media dos numeros:, media")