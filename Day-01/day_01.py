"""
Function returns the square root of the number if it is divisible by 5,
returns it`s remainder if it is not divisible by 5.
"""
def divide_or_square(num):
    result = (num ** 0.5) if (num % 5 == 0) else (num % 5)
    print(f"{result}" if isinstance(result, int) else f"{result:.2f}")

# test
divide_or_square(10)
divide_or_square(15)
divide_or_square(12)
divide_or_square(8)
