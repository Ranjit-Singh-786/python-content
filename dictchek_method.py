dictionary = dict.fromkeys([i for i in range(1,11)],'unknown')
l = dictionary.items()
#for i ,j in dictionary.items():
 #   print(i,j)
a , b = list(zip(*l))
print(list(a))
print(list(b))
c = tuple(zip(a,b))
#print(c)
for pairs in c:
    print(pairs)
