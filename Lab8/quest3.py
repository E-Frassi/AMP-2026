
import random
secreto = random.randint(1, 10)
chances = 5

while chances > 0:
    palpite = int(input("Adivinhe o número (1 a 10): "))
if 1<=palpite<=10:
    print("opção invalida, vce errou!")
    continue
chances =1
if palpite==secreto:
    print("parabens!!!!! acertou")
    break
print(secreto)