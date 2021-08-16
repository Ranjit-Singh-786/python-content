l1 = ['user1','user2','user2','user4']
l2 = ['harshit','ranjit','radhey','sachin']

print(zip(l1,l2))# here output zip object show
combine = list(zip(l1,l2))
print(dict(combine))
print(combine)

# this is output
#[('user1', 'harshit'), ('user2', 'ranjit'), ('user2', 'radhey'), ('user4', 'sachin')]
#and i want this output change the old position


print(tuple(zip(*combine)))# this is output          
#[('user1', 'user2', 'user2', 'user4'), ('harshit', 'ranjit', 'radhey', 'sachin')]
a,b = list(zip(*combine))
#print(a)
#print(b)#output
#('user1', 'user2', 'user2', 'user4')
#('harshit', 'ranjit', 'radhey', 'sachin')
print(list(a))
print(list(b))#old position
#['user1', 'user2', 'user2', 'user4']
#['harshit', 'ranjit', 'radhey', 'sachin']



l3 = [1,1,1,1,1,1,1,1]
l4 = [2,2,2,2,2,2,2]
l5 = list(range(1,8))
abc = list(zip(l3,l4,l5))
print(abc)

a,b,c = list(zip(*abc))
print(list(a))
print(list(b))
print(list(c))