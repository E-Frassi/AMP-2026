import random
import time
N=random.randint(0, 10)
for volta in range(1, N+1):
    print(f"Volta {volta}: Mais uma volta!")
    time.sleep(1)
print(f"Voltas: {N}")