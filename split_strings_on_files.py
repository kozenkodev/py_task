try:
    file_strings=[string.strip('\n') for string in open("domeni.txt",mode="r",encoding="utf-8").readlines()]
    counter=0
    for string in file_strings:
        file=open("{}.txt".format(counter),"w",encoding="utf-8")
        file.write(string)
        file.close()
        counter+=1
    input("Задача выполнена:создано {} файлов".format(counter))
except Exception as e:
    print("Произошла ошибка!")
    print(e)
    input("Проверьте наличие файлов!")
