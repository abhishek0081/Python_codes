# exception Handling
# try except else finally:
while True :
    try:
        age = int(input("Enter Your Age : "))
        break;
    except ValueError:
        print("Invalid Input .........");
    except:
        print("Unexpected Error !!!");
    else:
        print(f"user input = {age}");
        break
    finally:
        print("bsdk")



if age<18:
    print("You can't Play this game");
else:
    print("Move ahead");
