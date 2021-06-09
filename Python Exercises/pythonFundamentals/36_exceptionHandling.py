
# def divide(numerator, denominator):
#     try:
#         return numerator / denominator
#     except TypeError:
#         print('Got an error')
#         return int(numerator) / int(denominator)

# print('1' / 2)
# print(divide('1', '2'))
# print(divide('1', 0))

def divide(numerator, denominator):
    try:
        return numerator / denominator
    except (TypeError, ZeroDivisionError) as e:
        if e is TypeError:
            print('Got an error')
            return int(numerator) / int(denominator)

        print('You can\'t divide by zero!')
        return 0

print(divide('1', 0))