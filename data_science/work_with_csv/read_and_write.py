from csv import DictReader,DictWriter
with open("final.csv","r") as rf :
    with open("file2.csv","w",newline="")  as wf:
        csv_reader = DictReader(rf);
        csv_writer = DictWriter(wf,fieldnames=["First name","Last name","age"])
        csv_writer.writeheader();
        for row in csv_reader:
            fname,lname,age=row["First name"],row["Last name"],row["age"]
            csv_writer.writerow(
                {
                    "First name" : fname.upper(),
                    "Last name" : lname.upper(),
                    "age":age
                }
            )