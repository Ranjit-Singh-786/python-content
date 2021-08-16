# import time
# t1 = time.time()
# def cube_finder(n):
#     count = {}
#     for i in range(1,n+1):
#         count[i]=i**3
#     return count
# print(cube_finder(100))
# t2 = time.time()
# print(t2-t1)


# user_info = {
#     "name":"harshit","age":24,"score":85,"price":2500,
# }
# userietm = user_info.items()
# print(userietm)
# l2,l = list(zip(*userietm))
# list(l2)
# print(list(l))
# print(list(l2))
# # print(userietm)
# ab = list(zip(l,l2))
# print(dict(ab))
# print(type(userietm))


# user_info = {
#      "name":"harshit","age":24,"score":85,"price":2500,
#  }
# for i, j in user_info.items():
#     print(i,j)
# if user_info.get("name"):
#     # print(user_info["name"])
#     user_info["name"] = "radhey"
# else:
#     print("not present")
# print(user_info)


# word counter programe
# def word_counter(s):
#     counter = {}
#     for i in s:
#         counter[i] = s.count(i)
#     return counter
# a = input("please enter your string ")
# print(word_counter(a))


# dictionary create using user input


# user_info = {}
# name = input("enter your name ")
# age = input("enter your age ")
# fav_song = input("enter your song ").split(",")
# fav_movie = input("enter your movie name ").split(",")
# fav_tune = input("enter your tune ").split(",")
# user_info["name"] = name
# user_info["age"] = age
# user_info["fav_song"] = fav_song
# user_info["fav_movie"] = fav_movie
# user_info["fav_tune"] = fav_tune
# print(user_info)
# for key,value in user_info.items():
#     print(f"this is keys {key} and values is {value} ")



# student = {'name': 'harshit', 'age': '24', 'fav_song': ['s1', 's2', 's3', 's4'], 'fav_movie': ['m1', 'm2', 'm3', 'm4'], 'fav_tune': ['t1', 't2', 't3', 't4']}
# for i in student:
#     print(i)
# if "fav_movie" in student:
#     student["fav_movie"].insert(2,"m5")
#     student["fav_movie"].append("NASEEB")
# for k in student.items():
#     print(k)
# abc = student.items()
# a,v =list(zip(*abc))
# print(a)
# print(v)




# l = list(range(0,21))
# def chek(l,target):
#     for pos , item in enumerate(l):
#         if item == target:
#             return pos
# print(chek(l,5)) 



# cube_dict = {i:i**3 for i in range(1,11)}
# print(cube_dict)


# l = [2,1,4,5,8,7,6,9,3,2,21,24,25,26,27,29,24,22]
# print(list(filter(lambda a: a%2!=0  ,l)))
# print(list(filter(lambda a:a%2==0 ,l)))
# print(list(filter(lambda a:a==24,l)))
# print(list(filter(lambda a:a>=10 or a<=24 ,l)))
# t=list(filter(lambda a:a<10 ,l))
# s=list(filter(lambda a:a>10 ,l))
# print(s)
# print(t)
# \\\




# l = [2,1,4,5,8,7,6,9,3,2,21,24,25,26,27,29,24,22]
# def my_map(func,l):
#     new_list = []
#     for i in l:
#         new_list.append(func(i))
#     return new_list
# t =[]
# t2 = []
# for i in my_map(lambda a : a%2==0,l):
#     # print(i)
   
#     if i==True:
#         t.append(i)
#     else:
#         t2.append(i)
# print(t)
# print(t2)





# l = [2,1,4,5,8,7,6,9,3,2,21,24,25,26,27,29,24,22]
# true = list(map(lambda a : a%2==0 , l))
# print(true)
# even = []
# odd_list = []
# for i in true:
#     if i == True :
#         odd_list.append(i)
#     elif i == False:
#         even.append(i)
# print(odd_list)



class Phone:
    def __init__(self,model_name,brand_name,price):
        self.model_name = model_name
        self.brand_name = brand_name
        self.price = price
        self.complete_specification = model_name   + brand_name + price
    

    def full_name(self):
        return f"{self.model_name} {self.brand_name}"
obj = Phone("nokia","1200","3500")
print(obj.full_name())
print(obj.model_name)
print(obj.brand_name)
print(obj.price)