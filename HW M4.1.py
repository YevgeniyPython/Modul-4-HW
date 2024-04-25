from pathlib import Path

def total_salary(path):
    counter = 0
    amount = 0
    try:
        with open (path, "r", encoding='utf-8') as fh:
            while True:        
                lines = [el.strip() for el in fh.readlines()]
                for str in lines:
                    counter += 1
                    for i in str.split(","):
                        if i.isdigit():
                            amount += int(i)
                average_salary = int(amount/counter)
                return (amount, average_salary)
    except FileNotFoundError:
        print("Неможливо відкрити файл")
    except:
        print("Помилка при роботі з файлом")

# path1 = "D:/IT/Python Core 24/HomeWork/Modul 4/salary_file.txt"
# total, average = total_salary(path1)
# print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")     