#lambda expressions (anonymous function)

# def add(a,b):
#     return a+b


# add2 = lambda a,b : a + b
# print(add2(2,3))

# multiply =lambda a,b : a*b
# print(multiply(2,3))



#lambda expression practice






# def is_even(a):

#     return a %2 ==0

# print(is_even(5))
    # if a%2 ==0:
    #     return True
    # return False



# iseven2 = lambda a:a%2==0
# print(iseven2(5))

# last_char =lambda s :s[-1]
# print(last_char("Abhisek Kumar"))



#lamda if,else

def func(s):
    return len(s)>5
    #     return True
    # return False


Func = lambda s: len(s)>5

print(func("Abhisehk Kumar"))
print(Func("Ab"))