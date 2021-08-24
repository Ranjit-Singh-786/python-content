import numpy as np
from numpy.random import normal
# ,,,,,,,,,,,randint,,,,,,,,,,,,,,,

# single_int_value=np.random.randint(5)        # it will return only one elment in between 5
# more_int_value=np.random.randint(5,size=(10))  #it will return 10 element in between 5
# and_more=np.random.randint(4,size=(2,5))   # it will 2 row and 5 column in between 4

# ,,,,,,,,,,,,,rand,,,,,,,,,,,,,,,,

# one_num=np.random.rand(1)     #it will return only one element but element will be a float number
# two_num=np.random.rand(4)     #it will return 4 float number
# dimension_num=np.random.rand(2,5)    # it will 2 row and 5 columns with filling floating random number value

# ,,,,,,,,,,,randn,,,,,,,,,,,,,
# num=np.random.randn(1)           # it will only one floating number value
# num=np.random.randn(2)        #it will return 2 floating number
# num=np.random.randn(2,5)         # it wil return 2 row and 5 columns with filling floating point value

# ,,,,,,,,,,,,,,,,normal,,,,,,,,,,,,,,
# num=np.random.normal(1)             it will one floating point element
# num=np.random.normal(2,4)         # and till now also will be only one floating nuber

# ,,,,,,,,,,,choice,,,,,,,,,,,
lis=[i for i in range(1,7)]
num=np.random.choice(lis)

print('this is return a random number inside the list',num)



# print(single_int_value)    #4
# print(more_int_value)   #[1 2 3 1 1 1 0 1 2 0]
# print(and_more)
# output
# [[3 0 3 3 2]
#  [0 2 0 0 3]]
# print(more_num)