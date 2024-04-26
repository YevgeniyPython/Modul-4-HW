def get_cats_info(path):
    cats = [] 
    try:
        with open (path, "r", encoding='utf-8') as fh:
            while True:        
                lines = [el.strip() for el in fh.readlines()]
                for str in lines:
                    cat_info = {"id":"", "name":"", "age":""}
                    str = str.split(",")
                    cat_info["id"] = str[0]
                    cat_info["name"] = str[1]
                    cat_info["age"] = str[2]
                    cats.append(cat_info)
                return cats
    except FileNotFoundError:
        print("Неможливо відкрити файл")
    except:
        print("Помилка при роботі з файлом")
      
# path1 = "D:/IT/Python Core 24/HomeWork/Modul 4/Cats.txt"
# cats_info = get_cats_info(path1)
# print(cats_info)