def outer_func(x):
    print(f"this is your x value-------> {x} ")
    def inner_func(n):
        print(f"this is your n value------> {n} ")
        return f"this is your risult-------> {n**x} "
    return inner_func
# print(f" this is your x value {x} and this is your n value {n}")
var = outer_func(2)
print(var(2))