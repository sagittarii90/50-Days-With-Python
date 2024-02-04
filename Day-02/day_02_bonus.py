def check_duplicates(data_list) -> str:

    duplicates = [item for item in data_list if data_list.count(item) > 1]

    unique_item = list(set(data_list))

    # print(len(duplicates) if len(duplicates) > 0 else 'no duplicates')
    return len(duplicates) if len(duplicates) > 0 else 'no duplicates'


fruits = ['apple', 'orange', 'banana', 'apple']
names = ['Yoda', 'Moses', 'Joshua', 'Mark']
check_duplicates(fruits)
check_duplicates(names)