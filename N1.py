from pathlib import Path

def total_salary(path):
    p = Path(path)
    count_str = 0
    total_sum = 0
    average_sum = 0
    if(p.exists()):
        try:
            with open(p,"r",encoding="UTF-8") as file:
                for f_line in file:
                    count_str += 1
                    line_parts = f_line.strip().split(',')
                    if(len(line_parts) > 1):
                        total_sum += int(line_parts[1])
                    else:
                        print(f'У файлі для ',{line_parts[0]},' не вказана зарплатня')
                #Згідно очікуванного результату у завданні повертається int, але я б зробив float
                average_sum = int(total_sum/count_str)   
        except Exception as e:
            print('У файлі помилка: ', e)
    else:
        print("Файл не існує")
    return (total_sum,average_sum)

   
path = "text_files\salary_n1.txt"        
total, average = total_salary(path)
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}") 

