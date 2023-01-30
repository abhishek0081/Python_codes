from csv import writer

with open("file1.csv","w",newline="") as wf:
    csv_writer = writer(wf)
    # Methods - write Row , write Rows
    # csv_writer.writerow(["Name","Countries"])
    # csv_writer.writerow(["Abhishek kumar","INDIA"])
    # csv_writer.writerow(["Sujal Choudhary","INDIA"])

    csv_writer.writerows([["Name","Countries"],["Abhishek kumar","INDIA"],["Abhishek kumar","INDIA"]])
    
