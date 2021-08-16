student2 = {
    "mohit":{"score":85,"age":17},
    "raju":{"score":78,"age":27},
    "shyam":{"score":32,"age":18},
    "bhola":{"score":80,"age":16},
    "prem":{"score":39,"age":24},
    "chandan":{"score":48,"age":21},
    "kunal":{"score":74,"age":23}
}
print(max(student2 , key = lambda item :student2[item]["score"]))
print(type(student2))



student = [
    {"name":"harshit","score":86,"age":19},
    {"name":"shyam","score":78,"age":18},
    {"name":"bholla","score":88,"age":20},
    {"name":"rajuu","score":25,"age":27}
]
print(min(student , key= lambda a:a.get("score")))
print(min(student , key= lambda item:item.get("score"))["age"])


# ,,,,,print all the age of student dic ,,,,,,,,

for i in student:
    print(i.get("age"))