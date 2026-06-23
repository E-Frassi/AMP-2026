import random
import time
print("Prepare-se")
N=random.randint(2, 10)
time.sleep(N)
print("AGORA")
tempo_inicial=time.time()
input()
tempo_final=time.time()
tempo_reacao=tempo_final-tempo_inicial
print(f"Seu tempo de reação foi de {tempo_reacao:.3f} segundos.")