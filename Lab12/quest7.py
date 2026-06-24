import datetime
nome1=input("Nome da primeira pessoa: ")
data_str1=input("Data de nascimento (dd/mm/aaaa): ")
nome2=input("Nome da segunda pessoa: ")
data_str2=input("Data de nascimento (dd/mm/aaaa): ")
data1=datetime.datetime.strptime(data_str1,"%d/%m/%Y")
data2=datetime.datetime.strptime(data_str2,"%d/%m/%Y")
if data1<data2:
    print(nome1,"é mais velho.")
elif data2<data1:
    print(nome2,"é mais velho.")
else:
    print("As duas pessoas tem a mesma idade")