def only_floats(a, b):
    return len([x for x in (a, b) if isinstance(x, float)])


# only_floats(12.1, 23.4)
# only_floats(12.1, 23)
# only_floats(12, 23)

# print(only_floats(12.1, 23.4))
# print(only_floats(12.1, 23))
# print(only_floats(12, 23))
