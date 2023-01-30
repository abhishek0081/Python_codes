def multiply_nums(num1,num2,*args):
    multiply = 1
    print(num1)
    print(num2)
    print(args)
    for i in args:
        multiply *=i
    return multiply

print(multiply_nums(1,2,3,4))