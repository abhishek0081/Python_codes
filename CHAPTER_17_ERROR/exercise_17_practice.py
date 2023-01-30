def divide(a,b):
    return a/b;


while True :
    try:
        number1 = int(input("Enter number: "))
        number2 = int(input("Enter number: "))
        divide(number1,number2);
        print(divide(number1,number2));
        break;
    except ZeroDivisionError as err:
        print(err)
        # print("Dont enter denominator as 0 ");
    except (ValueError or TypeError) as error:
        print(error);
    else:
        break

