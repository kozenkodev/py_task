bag_content=[]
file_content=[string.strip('\n') for string in open("BASE.txt",mode="r",encoding="utf-8").readlines()]
type_remove=int(input("Введите 1 или 2\n 1 - удаление с начала строки\n 2 - удаление с конца строки:\n"))
count_chars=int(input("Введите количество символом для удаления:\n"))
if type_remove==1:
    for string in file_content:
        bag_content.append(string[count_chars:len(string)])
else:
    for string in file_content:
        bag_content.append(string[:-count_chars])

file=open("BASE.txt",mode="w",encoding="utf-8")
for item in bag_content:
    file.write(item+"\n")
print(bag_content)
print("Выполнено")
