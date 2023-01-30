user_info ={
    'name'  : 'Abhishek Kumar',
    'age'   :  20,
    'fav_movies' : ['shawshank redemption','tumbadd','phir hera pheri'],
    'fav_songs'  : ('redemption','old gods of asgard','Love language','take control')

}

# if 'name' in user_info:
#     print("presnet")
# else:
#     print("Not present")

# if 'Abhishek Kumar' in user_info.values():
#     print("Present")
# else:
#     print("Not Present")
# for i in user_info.values():
#     print(i)

# user_info_values =user_info.values()
# print(user_info_values)

# print(type(user_info_values))

# user_info_keys =user_info.keys()
# print(user_info_keys)

# print(type(user_info_keys))
# 

#items method

# dict_items =user_info.items()
# print(dict_items)
# print(type(dict_items))

for key,value in user_info.items():
    print(f"key is {key}  :   value is {value} ")