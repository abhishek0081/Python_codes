from csv import reader,DictReader
import csv

# with open("apple.csv","r") as rf:
#     csv_reader = reader(rf)  # iterator
#     # print(type(csv_reader))
#     next(csv_reader)
#     for row in csv_reader:
#         print(row)


with open("apple.csv","r") as rf :
    csv_reader = DictReader(rf)
    # csv_reader = DictReader(rf,delimiter=",")# if delimiter is different from "," then pass delimiter in Dictreader 
    next(csv_reader)
    for row in csv_reader:
        print(row["Date"])


        