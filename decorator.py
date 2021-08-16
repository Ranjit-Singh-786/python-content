# from functools import wraps
# def data_typ(data_tp):
#     def decorator(function):
#         print(decorator.__name__)
#         @wraps(function)
#         def wraper(*args,**kwargs):
#             # print(f"this is your function------> {wraps.__name__} ")
#             data_item = []
#             for arg in args:
#                 data_item.append(type(arg) == data_tp)
#             print(f" this is your lenght of adding number----> {len(data_item)} ")
#             if all(data_item):
#                 return function(*args,**kwargs)
#             print("invalid input !!")
#         return wraper
#     return decorator
# @data_typ(int)
def num_sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total
num = 1,2,3,4,5,6,7,8,9
print(type(num))
prin = num_sum(*num)
print(f" this is your number addition ---------> {prin} ")
        