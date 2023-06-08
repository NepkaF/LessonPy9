import csv
a=[]
minp = 9999999
with open("1.csv", encoding='utf-8') as r_file:
    # Создаем объект reader, указываем символ-разделитель ","
    file_reader = csv.reader(r_file, delimiter = ",")
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    count = 0
    # Считывание данных из CSV файла
    for row in file_reader:
        if count == 0:
            pass
        else:
            if float(row[5])>0 and float(row[5])<500:
                a.append(float(row[8]))
            if float(row[5])<minp:
                househ=row[6]
                minp=float(row[5])


        count += 1
print('Задача 40:')
print(sum(a)/len(a))
print('Задача 42:')
print(househ)