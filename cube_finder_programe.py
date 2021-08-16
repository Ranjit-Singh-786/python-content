# ,,,,,,,,,  (1)cuber finder programe append in dictionary


# def cube_finder(num):
#     cube = {}
#     for i in range(1,num+1):
#         cube[i] =i**3
#     return cube
# print(cube_finder(10))


#,,,,,,,,,,,,,, (2)  cube finder programe with the help of map function and lambda function 



# num = [1,2,3,4,5,6,7,8,9]
# c = list(map(lambda a: a**3 , num))
# print(c)

# ,,,,,,,,,,,(3)cube finder programe method 


def cube_finder(l):
    # return l**3
    cube = []
    for i in l:
        cube.append(i**3)
    return cube
print(cube_finder([i for i in range(1,21)]))
