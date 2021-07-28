n = list(range(1,11))
b = list(range(11,21))
e = lambda a: a.extend(b)    #lambda copy my list into the another list
#t = lambda a: a[2]*2    # and now here lamda calculate the index number 2
#t = lambda a: a*2       # here list repeat two times bcz lamda fatch the proper list in one time no iteration
k = lambda s: "true" if len(s)>=5 else "false"          #lambda function with the if and else statemenet
print(k("hrit"))
print(e(n))
print(n)
