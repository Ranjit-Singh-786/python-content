# this is simple trick if you want to 
# remove duplicacy in your list
d = [1,2,3,3,4,5,7,8,9]
print(type(d))
d = list(set(d))
print (d)
print(type(d))
