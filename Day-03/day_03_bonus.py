names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

def littel_symbol(list: list) -> tuple:
    new_names = []

    for item in list:
        if item[0] == item[0].lower():
            new_names.append(item)
    
    print(tuple(sorted(new_names, reverse=True)))
    return tuple(sorted(new_names))

littel_symbol(names) # -> ('kerry', 'dickson', 'carol', 'adam')