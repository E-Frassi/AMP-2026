import datetime

hoje=datetime.datetime.now()

data_prova=datetime.datetime(2026, 7, 14)

dif=data_prova-hoje

print("Faltam", dif.days, "dias para a prova.")