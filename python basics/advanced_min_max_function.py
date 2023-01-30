names ={
    "abhishek kumar",
    "sonu",
    "jayant",
    "Robin",
    "Sujal choudhary",
    "Ragini Choudhary",
    "Choti Choudhary",
    "Ram kumar choudahry",
    "Guriya Devi"
}
def func(item):
    return len(item)



print(max(names,key =lambda item:len(item)))
# print(max(names,key =func))

Student_marks =[
    {'name':'Abhishek kumar' ,'score':99,'age':21},
    {'name':'Sonu kumar' ,'score':91,'age':24},
    {'name':'Sony kumari' ,'score':81,'age':21},
    {'name':'Jayant kumar' ,'score':9,'age':24},
    {'name':'trisha kumar' ,'score':94,'age':21},
    {'name':'kemo kumar' ,'score':0,'age':21},
    {'name':'harshit kumar' ,'score':4,'age':24},
    {'name':'jaja kumar' ,'score':33,'age':21},
]

# print(max(Student_marks,key= lambda item:item.get('score'))['name'])


Student_marks2  = {
        'Abhishek kumar':{'score':99,'age':21},
        'Sonu kumar':{'score':91,'age':24},
        'Sony kumari' :{'score':81,'age':21},
        'Jayant kumari':{'score':9,'age':24},
        'trisha kar madhu' :{'score':94,'age':21},
        'kemo kumar' :{'score':1,'age':21},
        'harshit kumar':{'score':4,'age':24},
        'jaja kumar':{'score':33,'age':21},
}
# print(max(Student_marks2,key = lambda item:Student_marks2[item].get('score')))


# numbers = list(range(1,8));
# print(numbers)

names ={"Abhishek Kumar","Sonu Kumar","sujal"};
print(max(names,key = lambda item: len(item)));

students = {
    "abhishek" :{ "score" : 99,"age" : 21},
    "sujal" : { "score" : 91,"age":18},
    "sonu" : { "score" : 89,"age":22}
}

print(max(students,key=lambda item:students[item]["score"]));
print(max(Student_marks,key= lambda item:item.get("score"))["name"]);