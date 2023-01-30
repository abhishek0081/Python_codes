def multiply_nums(*args):
    multiply =1
    print(args)
    for i in args:
        multiply *=i
    return multiply

nums = list(range(1,41))
print(nums)
print(multiply_nums(*nums))