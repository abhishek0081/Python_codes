# with open("ex.txt","r") as r:
#     with open("salary.txt","w") as w:
#         for line in r.readlines():
#             w.write(line.replace(",","\tsalary is\t:"))
# alternate soln

with open("ex.txt","r") as r:
    with open("salary.txt","w") as w:
        for line in r.readlines():
            name,salary = line.split(",");
            w.write(f"{name} salary is {salary}")