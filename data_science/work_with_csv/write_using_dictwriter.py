from csv import DictWriter
with open("final.csv","w",newline="") as wf:
    csv_writer = DictWriter(wf,fieldnames=["First name","Last name","age"])
    csv_writer.writeheader()
    # csv_writer.writerow({
    #     "First name" : "Abhishek",
    #     "Last name"  : "Kumar",
    #     "age" : 21
    # })
    # csv_writer.writerows--------> [dict,dict,dict]
    csv_writer.writerows([
        {"First name":"Abhishek","Last name" : "Kumar","age": 21},
        {"First name":"Sujal","Last name" : "Choudhary","age": 18},
        {"First name":"Sonu","Last name" : "Raj","age": 21}
    ])

