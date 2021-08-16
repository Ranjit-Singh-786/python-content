# odd_even = {f"this is your number is {num} " : ('even' if num % 2 == 0 else 'odd')   for num in range(1,11)}
# # print(odd_even)
# for k,v in odd_even.items():
#     print(f"{k} : {v}")



dicti = {i : "even" if i % 2 == 0 else "odd" for i in range(1,21)}
print(dicti)
user = dicti.items()
d,f = list(zip(*user))
print(d)
print(f)
odd =[]
for i in f:
    if i == "odd" :
        odd.append(i)
print(odd)
print(f)
print(d)

