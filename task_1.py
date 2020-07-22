import re
base_storage=[]
file_A=[string.strip('\n') for string in open("А.txt",mode="r",encoding="utf-8").readlines()]
file_B=[string.strip('\n') for string in open("Б.txt",mode="r",encoding="utf-8").readlines()]
for number in file_A:
    for string in file_B:
        if str(re.findall(r'\d+',string)).__contains__(number) and string not in base_storage:
            print(string)
            print(number)
            base_storage.append(string)
if len(base_storage)>0:
    print("Было найдено следующие совпадения:")
    print(base_storage)
    print("Они записаны в файл Б")
    file_save=open("Б.txt",mode="w",encoding="utf-8")
    for string in base_storage:
            file_save.write(string+"\n")
    file_save.close()
else:
    print("Повторений не было найдено!")


