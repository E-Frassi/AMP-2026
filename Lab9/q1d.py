soma = 0
cont = 1
x = int(input("digite um valor:"))
while cont <= x:
    soma += cont
    cont += 1
    continue
if cont %2 == 0:
    print("a soma dos valores pares digitados é: ", soma)
    

        
    