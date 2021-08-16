def map2(func,l):
    new_list = []
    for item in l:
        new_list.append(func(item))
    return new_list
lis = map2(lambda a:a*2,[i for i in range(1,11)])
print(lis)  

disire element fatch to the list in between 5 to 15

def app(a):
    new = [] 
    for i in a:
        if i >= 5 and i<=15:
            new.append(i)
      
    return new
print(app(lis))
