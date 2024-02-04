from pathlib import Path

def get_cats_info(path):
    p = Path(path)
    name_of_attributes = ('id','name','age')
    cats_list = []
    if(p.exists()):
        try:
            with open(p,"r",encoding="UTF-8") as file:
                for f_line in file:
                    line_parts = f_line.strip().split(',')
                    dictionary = {'id': line_parts[0], 'name': line_parts[1], 'age': line_parts[2]}
                    cats_list.append(dictionary)
        except Exception as e:
            print('У файлі помилка: ', e)
    else:
        print("Файл не існує")
    return (cats_list)

   
path = "text_files\cats_n2.txt"        
cats_info = get_cats_info(path)
print(cats_info)