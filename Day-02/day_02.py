def convert_add(list: list) -> int:
    sum = 0
    for i in list:
        sum = sum + int(i)
    print(sum)

convert_add(['1','3','5']) # -->9