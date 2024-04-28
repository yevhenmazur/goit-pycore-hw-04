import sys
from pathlib import Path
from colorama import Fore, Style

try:
    p = Path(sys.argv[1])
except IndexError:
    print("Скрипт отримв невірну кількість аргументів. Переконайтеся що ви передаєте скрипту тільки один шлях до директорії")
    sys.exit()

def parse_file(path):
    '''The function print directory conten and hierarchy'''
    try:
        for el in path.iterdir():
            el_name = el.parts[-1]
            shift = "\t" * (len(el.parts) - 1)
            if el.is_dir():
                print(shift + Fore.BLUE + f"{el_name}" + Style.RESET_ALL)
                parse_file(el)
            else:
                print(shift + Fore.GREEN + f"{el_name}" + Style.RESET_ALL)
    except FileNotFoundError:
        print("Вказаного шляху не існує. Перевірте що шлях до директорії вірний")
    except NotADirectoryError:
        print("Не вдалося обробити шлях. Перевірте що вказуєте шлях до директорії")

parse_file(p)
