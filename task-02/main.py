def get_cats_info(path: str) -> list:
    '''
    This function processes information about cats. That's why everyone loves it.
    '''
    res = []
   
    try:
        with open(path, encoding='utf-8') as file:
            for line in file:
                line = line.split(",")
                individual_cats_dict = { \
                    "id": line[0], \
                    "name": line[1], \
                    "age": int(line[2]) \
                    }
                res.append(individual_cats_dict)
    
    except FileNotFoundError:
        print(f"Не вдалося знайти файл {path}.\nПеревірте його ім'я та правильність шляху")
        return None
    
    except IndexError:
        print("Не вдалося опрацювати файл!\nПеревірте що у кожній стрічці файла міститься інформація про кота у форматі id,name,age")
        return None

    return(res)

### Uncomment section below to check the function
# print(get_cats_info("task-02/cats.txt"))