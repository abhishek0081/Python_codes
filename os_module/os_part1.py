import os
# from typing import _get_type_hints_obj_allowed_types
# print(os.getcwd())  # current working directory
# create a folder

# while True:
#     l = input("Enter File name : ")
#     try:
#         os.mkdir(l)
#         break
#     except :
#         print("File Exists")
        
#             # raise FileExistsError

# open("file.xyz","a").close()
# os.mkdir(r"File director")


# listdir method

# print(os.listdir())


# to print path 
for item in os.listdir():
    print(os.path.join(os.getcwd(),item))




