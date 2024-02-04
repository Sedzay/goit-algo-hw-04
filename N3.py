import sys
from pathlib import Path
import colorama 

def visualize_directory(directory_path):
    directory_path = Path(directory_path)
    space = 0

    # Перевіряємо, чи існує директорія за вказаним шляхом
    if not directory_path.is_dir():
        print(f"Директорії '{directory_path}' не існує або це не директорія.")
        return

    # Функція для виведення файлів та директорій з кольоровим виділенням
    def print_colored(item, is_directory, space_loc):
        
        color = colorama.Fore.BLUE if is_directory else colorama.Fore.GREEN
        print(f"{' '*space_loc}{color}{item}")
        

    # Рекурсивна функція для обходу директорії
    
    def explore_directory(current_path,space_loc):
        
        for item in current_path.iterdir():
            if item.is_dir():
                print_colored(item.name, True, space_loc)
                explore_directory(item,space_loc+1)
            else:
                print_colored(item.name, False, space_loc)
            
            
    print_colored(directory_path.name, True,space)
    explore_directory(directory_path,space)

# Якщо не передан аргумент
if len(sys.argv) != 2:
    print("Використання: python N3.py /шлях/до/директорії")
else:
    # Викликаємо функцію для візуалізації директорії
    visualize_directory(sys.argv[1])

