# # # string formatting tools exercise
# # # str1 ="this is my string"
# # # # print(len(str1))
# # # # print("\n")
# # # # print(str1.find("my"))
# # # # print(str1.count('string'))
# # # # b =str1.replace("my","your")
# # # # b=str1.upper()
# # # # b=str1.lower()
# # # # print("this is \\\\ double backslash")
# # # # print('this is \t awesome' "this is backslash exam")
# # # # print('\n'"\t"+"\'")
# # # # print("/\\/\\/\\"'these are mountain')
# # # # print("\U0001f602")"this text used for emoji print"
# # # # string = "harshit is my freind"
# # # # if "g" in string:#here i could puted all string like:"harshit is my friend"
# # # #     print('present')
# # # # else:
# # # #     print("not present")
# # # age ke liye if else statement ka use
# # # # age = int(input("enter your age"))
# # # # # if 0>age or age>0:
# # # #     # print("your ticket is free")
# # # # if 10<=age:
# # # #     print("ticket price:-100")
# # # # elif 20<=age:
# # # #     print("ticket price :- 150")
# # # # elif 30<=age:
# # # #     print("ticket price :- 200")
# # # # else:
# # # #     print("your ticket price :- 250")
# # # # user input n number sum program......
# # # num =int(input("enter your number"))
# # # total = 0
# # # i = 1
# # # while i<=num :
# # #     total +=i
# # #     i = i+1
# # # print(total)
# # # table program n number.........
# # # n=int(input("enter your table number"))
# # # i=1
# # # while i<=10:
# # #     print(n,"*",i,"=",i*n)
# # # #     i=i+1
# # #,,,,,,,,,,,,,,,,,,, specifie center method and use user input..........
# # # n number sum using while loop....
# # # n=int(input("enter your name:-"))
# # # total = 0
# # # i = 1
# # # while i <= n:
# # #     total += i
# # #     i = i + 1
# # # print(total)
# # #,,,,,,,,,,,,,,, user n number input string number add programe...........
# # # num =input("enter your string :-")
# # # i = 0
# # # total = 0
# # # while i < len(num):
# # #      total =  total + int(num [i])
# # #      i += 1
# # # print(total)
# # # ,,,,,,,,,,,,,,,string ko count kro or print kro or uske sath index number bhi print kro..........
# # # .............program.................
# # # name = input("enter your name ")
# # # temp_var = " "
# # # i = 0
# # # b = 0
# # # while i < len(name):
# # #     if name[i] not in temp_var:
# # #         temp_var += name[i]
# # #         print(f"{name[i]} : {name.count(name[b])}")
# # #     i += 1
# # #     b += 1 
# #     #iski jagah ham kuchh bhi naa asign kre or b ki jgah pr i assign kr de koi bt nhi
# # #     enter your name ranjit singh
# # # r : 1
# # # a : 1
# # # n : 2
# # # j : 1
# # # i : 2
# # # t : 1
# # # s : 1
# # # g : 1
# # # h : 1
# # # .............program....................
# # # i am creating a programe using by for loop 
# # # this program print hello world ten times with rangefunction
# # # for i in range(1,25,2):
# # #     print(f"jigar my LOVE  {i} ")
# # #     print("I AM RADHEY \n")
# # # ...........program................
# # n = input("enter the number ")
# # n =int(n)
# # total = 0
# # for i in range(1,n+1):
# #      total = total + i #total +=i
# #      print(total)

# # # .......for horizontally print..............
# # for i in range(1,11):
# #     print(i,end =",")
# # ,,,,,,,,,,,,,this is example of global keyword accessing,,,,,,,,,,,,,,,,,
# # var = 5
# # def fuc():
# #     global  var
# #     var += 15
# #     return var
# # print(fuc())
# # ,,,,,,,,,,,,,,,,,,list program  operATION,,,,,,,,,
# # fruit =['mangoes','banana','apple','grapes']
# # print(fruit)
# # print(sorted(fruit))
# # print(fruit.clear())
# # print(fruit)
# # print(fruit.sort())
# # ,,,,,,,for copy a new list,,,,,,,,,,,,
# # fruits = fruit.copy()
# # print(fruits)
# # ,,,,,,,,,,extend method in list,,,,,,,,,,,
# # ,,,,,,,,,,this is  syntex wrong or i dont know why is not runing,,,,,,,
# # fruit =['mangoes','banana','apple','grapes']
# # fruits = ['radhey']
# # print(fruit.extends(fruits))
# # ,,,,,,,,,,,,,print reverse string using by function,,,,,,,,,,,,,,,,,,,
# # def chok(l):
# #     element = []
# #     for i in l:
# #         i[::-1]
# #         element.append(i[::-1])
# #     return element
# # num = ['xyz','tuv','abc']
# # print(chok(num))
# # ,,,,,,,,,,,,,,,,,,,list exercise programe,,,,,,,,,,,,,,,
# # def odd_even(l):
# #     odd_num = []
# #     even_num = []
# #     for i in l:

# #         if i%2 == 0:
# #             even_num.append(i)
# #         else:
# #             odd_num.append(i)
# #     # return odd_num +even_num#ise bhi use kr skte ho and
# #     output =[even_num,odd_num]  # but this is right way 
# #     return output     
# # num =list(range(1,25))#this list was created by using range function
# # print(odd_even(num))  
# # ,,,,,,,,,,,,,,,,,,,,list ecercise program,,,,,,,,,,,,,,,
# # def common_finder(l,l2):
# #     output = []
# #     for i in l:
# #         if i in l2:#here compairing both of table
# #             output.append(i)#here appending
# #     return output
# # num1 = list(range(0,25))
# # num2 = list(range(15,35))
# # common_value = common_finder(num1,num2)#here i am assigning the function in the vareible
# # print(common_value)
# # ,,,,,,,,,,,,MIN and MAX using a program,,,,,,,,,,,,,,,,,,,,,,,
# # num = list(range(25,88,2))
# # def min_max(l):
# #     return max(l) - min(l)
# # calculation = min_max(num)
# # print(num)
# # print(f"this is your calculation max value minus minimum value is {calculation} ")
# # ,,,,,,,,,,,,,checking program and counting program how many list in insinde list,,,,,,,,,,,,,,,,
# # mixed = [1,2,3,4,[5,4,8,7,5],[8,7,9,6,5],[1,4,5,4,5]]
# # def counterr(l):
# #     count = 0
# #     for i in l:
# #         if type(i) == list:
# #             count = count + 1
# #     return count
# # calculte_list = counterr(mixed)
# # print(f"this is your list inside the side  {calculte_list}")
# # ,,,,,,,,,,,,,,,,,,,,,,,,tuple programe exercise return two value,,,,,,,,,,,,,,,
# # def add_two(num1,num2):
# #     add = num1 + num2
# #     multi = num1 * num2
# #     return add,multi
# # print(add_two(2,3))#if i print this code so output become a tuple but
# # #   ooutput :-  (5, 6)
# # add,multi = add_two(2,3)
# # print(add) #out become a integer value this code
# # print(multi)
# # output:- 5,6
# # ,,,,,,,,,,,,,,,,tuple exercise tuple in list,,,,,,,,,,,,,
# # tupe1 = ('one','two','three',[1,2,3,4])
# # print(type(tupe1))
# # #if you want changes in your list inside the tuple so ussed this method
# # print(tupe1[3].pop())
# # tupe1[3].append([5,6,7,8,9]) # ('one', 'two', 'three', [1, 2, 3, [5, 6, 7, 8, 9]])
# # # print(tupe1[3][1][2]) # ye ese hi mene kuchh jyda advance krne ki kosis ki thi
# # print(tupe1)
# # ,,,,,,,,,,,,dictionary start,,,,,,,,,,,,, 
# dic1 = {'mango':25,'banana':30,'apples':80,'fav_movie':['terenam','jigar','bajrangi_bhaijan']}

# print(type(dic1))
# .,,,,,,,,,,,,,,,,,,,,all set operation remove duplicay method in the list ,,,,,,,,,,,,,,,,,,
# d = [1,2,3,3,3,4,4,5,8,7,9,6,8,]
# d = set(d)
# d = list(set(d))
# print(f" this is my list {d} ,and this is type of list {type(d)} ")
# d = [1,2,3,3,3,4,4,5,8,7,9,6,8,]
# d = set(d)
# d.add(15)
# d2 = d.copy() file copy ho jayegi
# d2.pop()# randomly dleate kr dega
# d.remove(11)#error show nhi hoga
# d.discard(11)
# d2 = {1,11,12,2,22,1,4,7}
# s = d & d2 #intersection method commom element find method
#s = d | d2 # union method add two set and remove duplicay
# print(d)
# ,,,,,,,,,,,,,list comprehension program............1
# name = ['harshit','mohit','rohit']
# name_list = []
# for items in name:
#     name_list.append(items[0])
# print(name_list)
# ,,,,,,,,,,,,according to list comprehension,,,,,,,,,,,,,,,1
# name_list = [item[0] for item in name]
# print(name_list)
# ,,,,,,,,,,,reverse string print program,,,,,,,,,,,,,,,,,,,2
# name = ['harshit','mohit','rohit']
# name_list = []
# for i in name:
#     name_list.append(i[::-1])
# print(name_list)
# ,,,,,,,,,,,,,accornding to list comprehension,,,,,,,,,,,,,,,,3
# name_list = [i[::-1] for i in name]
# print(name_list)
# ,,,,,,,,,,,,,even number append program,,,,,,,,,,,,,,,,,,,,,,,4
# even_list = []
# for i in range(1,21):
#     if i%2==0:
#         even_list.append(i)
# print(even_list)
# ,,,,,,,,,,,,this program according to list comprehension,,,,,,,,5
# even_list = [i for i in range(1,21) if i%2!=0]
# print(even_list)
# ,,,,,,,,,,,,,,odd number append in empty list program using comprehension,,,,,,,,,,,,,,6
# odd_list = ["even" if i%2==0 else "odd" for i in range(1,21) ]
# even = []
# odd = []
# for i1 in odd_list:
#     if i1 == "even" :
#         even.append(i1)
#     else:

#         odd.append(i1)
# print(even)
# print(odd)

# print(odd_list)
# ,,,,ek esa program jisme list pass ki jayegi or list me se int or float type ke eliment ek nyi list me append krna,,7
# def apend_func(l):
#     return [str(i) for i in l if type(i)==int or type(i)==float]
# liss = ['harshit',True,False,25,50,2.5,5.2]
# print(apend_func(liss))
# for item in liss:
#     print(f" this is my item {item} : {type(item)} ")


# ,,,,,,,,,,,,this program according to simple way,,,,,,,,,,,,,,,

# list1 = ['harshit','mohan',25,50,2.5,5.2]
# str1 = []
# for i in list1:
#     if (type(i)==int or type(i)==float):
#         str1.append(str(i))
# print(str1)



# ,,,,,,,,,,,,,,,according to list comprehension,,,,,,,,,,,,,

# def appen_func(l):
#     return [str(i) for i in l if (type(i)==int or type(i)==float)]
# print(appen_func(['harshit','mohan',25,50,2.5,5.2]))


# ,,,,,,,,,,ordere of all parameter in function............

# def func(name, *roll, age = 19, **kwargs):  # * gather as tuple
#     print(f'name is :{name} ')
#     print(f'roll number is  {roll} ')         #** gather as dictionary
#     print(f'age is {age} ')
#     print(f'this is subject {kwargs}')
# d = {"math":55, "sceinces":75}
# b = tuple(range(1,6))
# func('harshit', *b , 25 ,**d)




