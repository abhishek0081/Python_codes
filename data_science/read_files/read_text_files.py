#readfile
# open function
# read method
#seek method # to change cursor position
# tell method #to find where is our cursor
# readline method  # to read one line at one time
# readlines method
# close method

f = open("data.txt","r") # returns object
# print(f"cursor position {f.tell()}")
# print(f.readlines())
# print(f.readline())
# print(f"cursor position {f.tell()}")
# f.seek(0)  # to change cursor position
# print(f.read())
# print(f"cursor position {f.tell()}")

# lines = f.readlines()
# for line in lines:
#     print(line,end= "")
# data discreptor
# 1) .name
# 2) .closed
# f = open(r"D:\OneDrive\Desktop\python\data_science\read_files\read_text_files.py")
# f = open(r"D:/OneDrive/Desktop/python\data_science/read_files/read_text_files.py")
for line in f:
    print(line,end="")
print(f.closed)
print(f.name)
f.close()

