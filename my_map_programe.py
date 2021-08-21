numbers = list(range(1,21))
def my_map(func,i):
    new_list = []
    for item in i:
        new_list.append(func(item))
    return new_list
def square(a):
    return a**2
print(my_map(square,numbers))

# ,,,,,,,,,,,only one line using create this programe,,,,,,,,,,,

# print(list(map(lambda a : a**2 ,list(range(1,21)))))


# ,,,,,,,,,,Now i will also calling with the help of lamvda expression,,,,,,,,,,


# print(my_map(lambda a:a**2,numbers))

# ,,,,,,,,,,,,accordint to list comprehension create map function,,,,,,,,,,,,


# def my_map(func,i):
#     return [func(item) for item in i]
# print(my_map(lambda a:a**2,numbers))
    