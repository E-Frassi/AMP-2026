import datetime
nome1=input("Digite o nome da primeira pessoa: ")
data_str1=input("Digite a data de nascimento (dd/mm/aaaa): ")
nome2=input("Digite o nome da segunda pessoa: ")
data_str2=input("Digite a data de nascimento (dd/mm/aaaa): ")
data1=datetime.datetime.strptime(data_str1, "%d/%m/%Y")
data2=datetime.datetime.strptime(data_str2, "%d/%m/%Y")
hoje=datetime.datetime.now()
aniv1=datetime.datetime(hoje.year, data1.month, data1.day)
aniv2=datetime.datetime(hoje.year, data2.month, data2.day)
if aniv1<hoje:
    aniv1=datetime.datetime(hoje.year+1, data1.month, data1.day)
if aniv2<hoje:
    aniv2=datetime.datetime(hoje.year+1, data2.month, data2.day)
dias1=(aniv1-hoje).days
dias2=(aniv2-hoje).days
if dias1<dias2:
    print("O aniversário mais próximo é o de", nome1)
elif dias2<dias1:
    print("O aniversário mais próximo é o de", nome2)
else:
    print("Os aniversários são no mesmo dia.")