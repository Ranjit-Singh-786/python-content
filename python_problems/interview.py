# 1. Given a list of numbers, write a Python function to find the sum of all even numbers in the list.
# def sum_of_even(lst):
#     a = 0
#     for i in lst:
#         if i%2==0:
#             a+=i
#     return a

# sumision = sum_of_even([2,2,1,2])
# print(sumision)

# 2. Write a Python function that takes a string input and returns the count of
# each character in the string as a dictionary.

# def string_count(strin):
#     """ it cares about the case.
#     you can lower all of them string.lower() then count
#     """
#     dic = {}
#     # strin = strin.lower()
#     for i in strin:
#         dic[i] = strin.count(i)
#     print(dic)

# print(string_count.__doc__)
# string_count('Harshit')


# 3. Implement a Python class for a simple stack data structure that supports push, pop, and peek operations.
# from typing import List
# class stack_class:
#     def __init__(self,stack:List):
#         self.stack = stack

#     def push_op(self,element):
#         element_pushed = self.stack
#         element_pushed.append(element)
#         return f" element pushed {element_pushed}"
    
#     def pop_op(self):
#         popped_element = self.stack.pop()
#         return f"element poped {popped_element}"

#     def peek(self):
#         """
#         Returns the item from the top of the stack without removing it.
#         """
#         if len(self.stack) != 0:
#             return self.stack[-1]


#     def show(self):
#         return self.stack
    
# stack = stack_class([])
# puse_element = stack.push_op(100)
# puse_element = stack.push_op(150)
# puse_element = stack.push_op(200)
# print(puse_element)

# poped_item = stack.pop_op()
# print(poped_item)

# print(stack.peek())

# print(stack.show())

# 3. Given a sorted list of integers, write a Python function to find the index
#    of a target value using binary search.
# binary search if target True return index if False then do nothing

# def return_target_index(listt,target):
#     dic = dict()
#     print(f'your list :- {listt} and target :- {target}')
#     for index,element in enumerate(listt):
#         if element == target:
#             dic[element] = index

#     return f"this is your result {dic}"

# result = return_target_index(list(range(2,100)),4)
# print(result)


# 4. Write a Python function to check if a given string is a palindrome
#  (reads the same backward and forward) ignoring spaces and punctuation.

# def palindrome_check(stringg):
#     print(stringg)
#     if stringg == stringg[::-1]:
#         print(f'this is palindrome string :- {stringg}')
#     else:
#         print(f"this is not palindrome string :- {stringg}")
    
# palindrome_check('kanak2')

# 5. Given a list of integers, write a Python function to find the maximum product of
#    any three numbers in the list.

from typing import List
# def max_product_of_the_element(lis:List):
#     sorted_list_desc = sorted(lis,reverse=True)
#     max_amount = sorted_list_desc[0]*sorted_list_desc[1]*sorted_list_desc[2]
#     print(f'maximum element {(sorted_list_desc[0],sorted_list_desc[1],sorted_list_desc[2])} and result is :- {max_amount}')

# max_product_of_the_element([25,25,41,85,74,58,65,45,85])


# 6. permutaion combination with two length, not return any common combination.
# def permutation_combination(lst):
#     lst = list(set(lst))
#     combinations = []
#     n = len(lst)
#     for i in range(n):
#         for j in range(i + 1, n):
            
#             combinations.append((lst[i], lst[j]))
#     return combinations
# print(permutation_combination([1,2,3,3]))

# 7.    # Given a matrix represented as a list of lists, 
    # write a Python function to rotate it 90 degrees clockwise.

# a =[[1,2,3],[4,5,6],[7,8,9]]
# def metric_rotate(a:List):
#     print(a)
#     print()
#     main_metrix = []
#     for row in range(len(a)):
#         temp_list = []
#         for col in a:
#             temp_list.append(col[row])
#         temp_list.reverse()
#         main_metrix.append(temp_list)
#     return main_metrix

# rotated_metrics = metric_rotate(a)
# print(rotated_metrics)


# 8. Transpose List program

# import numpy as np
# a =[[1,2,3],[4,5,6],[7,8,9]]
# def Transpose(a:List):
#     transpose_list = []
#     for i in range(len(a)):
#         temp_list = []
#         for j in a:
#             temp_list.append(j[i])
#         transpose_list.append(temp_list)
#     return np.array(transpose_list)

# transposed = Transpose(a)
# print(transposed,'\n')
# b = np.array(a)
# print(b.T)


# 9. Implement a Python function to find the first non-repeated character in a string.

# string = "hhrshit"
# temp = 0
# for i in string:
#     for j in range(1,len(string)-1):
#         if (i != string[j]) and (temp == 0):
#             print(f" this is string :- {string} this is your result :- {string[j]}")
#             temp+=1
#         if temp>0:
#             break
    

# 10.Reverse a sentence without reversing the words in Python.

# sentence = 'you are python programmer'
# word_list = sentence.split()
# print(word_list[::-1])

# 11. Remove duplicates from a sorted list.
# there are two say, you can directly use the set() method

# lst = [1,2,3,3,4,4,5,6,7,8,9,2,5,3]
# def remove_duplicate(lst):
#     temp = ''
#     for i in range(len(lst)):
#         for j in range(i,len(lst)):
#             if str(lst[i]) not in temp:
#                 temp = temp+str(lst[i])+' '
#     new_list = temp.split(' ')
#     new_list.remove('')
#     return new_list
# print(remove_duplicate(lst))


# 11. implement Binary Search Algorithym. BST always in ascending order

# def Binary_search_algo(lst,target_element):
#     lower_bound = 0
#     upper_bound = len(lst)-1           ## <---- Focus
#     position = 0
#     while lower_bound<=upper_bound:
#         # to get the mid point
#         mid_point = (upper_bound+lower_bound)//2

#         if lst[mid_point] == target_element:
#             position = mid_point
#             print(lst,'\n')
#             print(f'index :- {position} and element on which this index :- {lst[mid_point]} ')
            
        
#         if lst[mid_point]<target_element:
#             upper_bound = mid_point
#         else:
#             lower_bound = mid_point

# testing_list = [2,4,6,8,9,12,14]
# Binary_search_algo(testing_list,14)

# 12. Implement a Python function to calculate the power of a number without using the built-in ** operator.
      

# def power(n):
#     def on_number(x):
#         result = x**n
#         return result
#     return on_number
# on_number = power(2)
# result = on_number(4)
# print(result)


# 13. Write a Python program to find the common elements between two lists

# def find_common_element(lst1,lst2):
#     temp_list = []
#     for i in lst1: 
#         for j in lst2:
#             if i == j:
#                 temp_list.append(i)
#     return temp_list

# ls1 = list(range(1,11))
# ls2 = [14,54,35,2,4,5,65,14,78,54]
# common_element = find_common_element(ls1,ls2)
# print(f"this is all your common element :- {common_element}")


# 14.Given a list of integers, write a function to find the maximum sum of any two elements 
# that are not adjacent to each other.

# def maxsum_not_adjacent(lst1):
#     lst1.sort(reverse=True)
#     max_sum_of_two_no = lst1[0]+lst1[2]
#     return max_sum_of_two_no

# ls2 = [14,54,35,2,4,5,65,14,78,54]
# arr = [1, 2, 3, 4, 5]
# output = maxsum_not_adjacent(arr)
# print(f"maximum sum of two element but not will be adjacent :- {output} ")

# 15. pattern program
# OUTPUT
# enter row :- 5
# * 
# * *
# * * *
# * * * *
# * * * * *

# enter_no_row = int(input('enter row :- '))
# for row in range(1,enter_no_row+1):
#     for col in range(1,row+1):
#         print('*',end=" ")
#     print()

# 16. pattern
# enter row :- 5
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5



# row = int(input('enter row :- '))
# for row in range(1,row+1):
#     for col in range(1,row+1):
#         print(col,end=' ')
#     print()




# 17. enter row :- 5
# * 
# * * *
# * * * * * 

# row = int(input('enter row :- '))
# for row in range(1,row+1,2):
#     for col in range(1,row+1):
#         # if col%2==0:
#         #     # print('*',end=' ')
#         #     continue
#         print('*',end=' ')
#     print()


# 18.
# enter row 8
#        *
#       * *
#      * * *
#     * * * *
#    * * * * *
#   * * * * * *
#  * * * * * * *
# * * * * * * * *


# row = int(input('enter row '))
# for i in range(0,row):
#     # loop for space
#     for j in range(0,row-i-1):      #  <--- Focus in range
#         print(end=' ')
#     # loop for print *
#     for k in range(0,i+1):
#         print('*',end=' ')
#     print()


# 19
# enter row number :- 6
# * * * * * * 
#  * * * * *
#   * * * *
#    * * *
#     * *
#      *

# num = int(input('enter row number :- '))
# for row in range(num,0,-1):
#     #loop for space
#     for space in range(0,num-row):
#         print(end=' ')
#     # loop for print *
#     for star in range(0,row):
#         print('*',end=' ')
#     print()

# 20. string count plus return char which is mostly occured

# def string_count(string):
#     frequence = {}
#     for i in string:
#         frequence[i]= string.count(i)
#     print(f"this is frequency count :- {frequence} \n")
#     d = list(frequence.values())
#     max_element = max(d)
#     for key,value in frequence.items():
#         if value == max_element:
#             print(f"this is char :- {key} and Highest occurences :- {value}")

# string_count('harshit')


# 21. 'this is my book'
#      siht si ym koob

# def reverse_each_word(srt):
#     srt = srt.split()
#     reverse_word_list = []
#     for word in srt:
#         reverse_word_list.append(word[::-1])
#     # now join all words as string
#     output = ' '.join(reverse_word_list)
#     return output

# st = 'this is my book'
# output = reverse_each_word(st)
# print(st,'\n')
# print(output)


# 22. remove all duplicate character from the sting,
#  if you used set then it will maintain the order of the list

# exmpl = 'javaaakaallabhuktkdkakkkdldfglkgdgkdglg'
# lis = []
# test = ''

# for i in range(len(exmpl)):
#     lis.append(exmpl[i])


    
#     if exmpl[i] not in test:
#         test+=" "+exmpl[i]
 
# st = list(set(lis))
# output = ' '.join(st)
# print('output get by two way ')
# print(f"output by set function :- {output.upper()}")
# print(f"output from scratch :- {test.upper()}")

# 23. generate an infinite fibonacci series, by using generator
# def febonacci_with_while():
#     sum = 0
#     n1 ,n2 = 0,1
#     while True:
#         print(sum,end=" ")
#         n1 = n2
#         n2 = sum
#         sum = n1 + n2
        
# febonacci_with_while()
# 24. sort a list without using sort builtin function in ascending order

# def sort(lst):
#     for i in range(0,len(lst)):
#         for j in range(i+1,len(lst)):
#             if lst[i]>lst[j]:   #<-- it is for ASC and use < for DESC.
#                 temp = lst[i]
#                 lst[i] = lst[j]
#                 lst[j] = temp
#     return lst
# test_list = [25,14,52,45,65,85,47,85,124,5,95,25,48,54,96]
# sorted_list = sort(test_list)
# print(sorted_list)

# 25. sort a dictionary and or sort a dictionary by using dictionary comprehension
# my_dict = {'apple': 3, 'banana': 1, 'cherry': 2, 'date': 4}
# # sort by key
# new = {key:my_dict[key] for key in sorted(my_dict)}
# print(new)


# dictionary sort by value  

# sorted_value = sorted(my_dict.values())
# new_dic = dict()
# for value in sorted_value:
#   for key , val1 in my_dict.items():
  
#     if val1 == value:
#       new_dic[key] = value
# print(new_dic)







# 26. create a fibonacci series by using recursion

# def febonacci(num):
#     n1,n2 = 0,1
#     sum = 0
#     for i in range(0,num):
#         print(sum,end=" ")
#         n1 = n2
#         n2 = sum
#         sum = n1 + n2
# febonacci(7)


# def febonacci_with_while():
#     num = int(input('enter number :- '))
#     sum = 0
#     n1 ,n2 = 0,1
#     i = 0
#     while i < num:
#         print(sum,end=" ")
#         n1 = n2
#         n2 = sum
#         sum = n1 + n2
#         i+=1
# febonacci_with_while()


# 27. find min and max element from the list without using any builtin function

# def find(lst:List,min_or_max:str):

#     if min_or_max=='min':
#         min = lst[0]
#         for i in range(1,len(lst)):
            
#             if min > lst[i]:
#                 min = lst[i]
#         return min
#     elif min_or_max == 'max':
#         max = lst[0]
#         for j in range(1,len(lst)):
            
#             if max < lst[j]:
#                 max = lst[j]
#         return max
# test_list = [25,14,52,45,65,1,47,85,1000,124,5,95,25,48,54,96]
# min = find(test_list,'min')
# print(min,'\n')
# max = find(test_list,'max')
# print(max)

# 28. while prectise
# a = 0
# while (a <= 5):
#     for i in range(0,5):
#         print('jai bhim')
#     print(a)

#     if a == 4:
#         break
#     a+=1
