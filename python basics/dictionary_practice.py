user_info ={
}

name =input("Enter Your name  : ")
age =input("Enter Your age  : ")
Fav_movies = input("Enter your favourite movies comma seperated  : ").split(",")
Fav_songs =input("Enter Your Favourite Songs comma seperated  : ").split(",")

user_info['name']=name
user_info['age']=age
user_info['Fav_movies']=Fav_movies
user_info['Fav_songs']=Fav_songs


for key,value in user_info.items():
    print(f"key is {key}  :   value is {value} ")

