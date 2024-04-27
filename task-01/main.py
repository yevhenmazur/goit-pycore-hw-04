def total_salary(path: str) -> tuple[(int, float)]:
    '''
    The function analyzes the file and returns the total and average salary of all developers.
    '''
    sum = 0
    med = 0
    count = 0
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                line = line.split(",")
                sum += int(line[1] )
                count += 1
            med = sum / count
    except FileNotFoundError:
        print(f"Не вдалося знайти файл {path}.\nПеревірте його ім'я та правильність шляху")
        return None
    
    except IndexError:
        print("Не вдалося опрацювати файл!\nПеревірте що у кожній стрічці файла міститься м'я працівнка і його зарплата, розділені комою")
        return None

    return((sum, med))

### Uncomment section below to check the function
print(total_salary("task-01/text.txt"))