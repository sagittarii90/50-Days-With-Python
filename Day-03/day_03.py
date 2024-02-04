register = {'Michael':'yes', 'John':'no', 'Peter':'yes', 'Mary':'yes'}

def register_check(dict) -> int:
    count_children = 0

    for key,value in dict.items():
        if value == 'yes':
            count_children = count_children + 1
                
    print(count_children)
    return count_children
    


register_check(register)