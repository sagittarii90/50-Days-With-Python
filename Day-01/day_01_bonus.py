def longest_value(dict):
    
    # Знайдемо ключ з найбільшою довжиною значення
    max_key = max(dict, key=lambda k: len(str(dict[k])))

    # Повертаємо значення, що відповідає знайденому ключу
    return dict[max_key]
    

dict1 = {'Car': 'Audi', 'color': 'black'}
dict2 = {'Car': 'Mercedes-Benz', 'color': 'yellow'}

print(dict1)
longest_value(dict1)

print(dict2)
longest_value(dict2)