name = input("search here:- ")
my_friend_list = ["rahul","shakeel","sahil","raghav","mosim","shivam","arjun","vishal","karan","shiva","ajit singh","ashis","mohan","sanjay","babu",]
data={"rahul" :[["NAME-RAHUL SHARMA"],["LIVES-IN:-HATHRAS"],["STUDYING IN-IET AGRA UNIVERSITY"]],"mohan" :[["NAME-Mohan chaudhary" ],["LIVES-IN:-Aligarh"],["STUDYING IN-AMU Aligarh university"]],
"babu" :[["FULL-NAME- SANDEEP KUMAR" ],["LIVES-IN:-TELANGANA"],["STUDYING IN-SRS inter college bahardoi "]]}



my_friend_of_friend=["priyanshu","saurabh","suneel","ramkumar","akshay","shivam","sahil ali","vinod","santosh","deepak"]

data2={"priyanshu" :[["NAME-priyanshu SHARMA"],["LIVES-IN:-mirjapur"],["STUDYING IN-IET AGRA UNIVERSITY"]],"shivam" :[["NAME-shivam tiwari" ],["LIVES-IN:-Alahabad"],["STUDYING IN-MG polytechnic hathras"]],
"saurabh" :[["FULL-NAME- Er.Saurabh sir" ],["LIVES-IN:-mummai"],["STUDYING IN-IIT Roraki "]]}

for i in my_friend_list:

    if i==name:
        print("this is my friend :- ",i)
        print()
        print(f"if you want to more information {i} TYPE 'YES' otherwise type 'NO'" )
        condi = ["yes"]
        info = input()
        if info in condi:
            if i in data:
                for i in data[i]:
                   print(i)



    else:
        for i in my_friend_of_friend:


            if i==name:


                print("this is your friend of friend :- ",i)
                print()
                print(f"if you want to more information {i} TYPE 'YES' otherwise type 'NO'" )
                condi = ["yes"]
                info = input()
                if info in condi:

                    if i in data2:

                        for i in data2[i]:
                            print(i)
print("THIS RECORD IS NOT MATCHED MY DATA BASE")
        
    








    # ,,,,,,,,,,,here comment part for prectice,,,,,,,,,,



    # else:
    #     print("this is not your friend")
    #     break 
            

# "NAME-Rahul Singh,,LIVES-Hathras,,STUDY IN- IET AGRA"
# "NAME-Mohan Sharma,,LIVES IN-Aligarh,,STUDY IN-AMU University"



# a="rahul"
# a="RAHUL"
# print(a)
# print(a == b.lower())
# a= "ram"
# b="kam"
# c="syam"
# d="mohan"
# data=[a,b,c,d]
# for i in data:
#     if "ram"==i:
#         print("this is your database record")

# data={"rahul":[[NAME-RAHUL SHARMA],["LIVES-IN:-HATHRAS"],["STUDYING IN-IET AGRA UNIVERSITY"]]}
# if "rahul" in data:
#     print("present here")
#     print(data["mohan"])
    # print(rahul.values()) 
# dict inside list chek kro abhi ok for better risult 
# tdl=[["NAME-RAHUL SHARMA"],["LIVES-IN:-HATHRAS"],["STUDYING IN-IET AGRA UNIVERSITY"]]
# print(type(tdl))
# print()
# # print(tdl)
# for sublist in tdl:
#     print(sublist)
# cond=["yes"]
# if "yes" in cond:
#     print("present here")
# else:
#     print("not present here")
