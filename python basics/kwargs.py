# kwargs (keyboard arguments)
# kwargs (Double star arguments)

# kwargs as a parameter
def func(**kwargs):
    # print(kwargs)
    # print(type(kwargs))
    for k,v in kwargs.items():
        print(f"{k} :  {v }")


# func( name =  'Abhishek Kumar',Age = 21)
# Dictionary unpacking
user_info ={
    'name'  : 'Abhishek Kumar',
    'age'   :  20,
    'fav_movies' : ['shawshank redemption','tumbadd','phir hera pheri'],
    'fav_songs'  : ('redemption','old gods of asgard','Love language','take control')

}
func(**user_info)
