# functions with all parameters
# very important to understand

#PADK

#Parameters
#args
#default parameters
#kwargs


# def func(name='unknown',age=2):
#     print(name)
#     print(age)

# func('abhhishek',21)

def func(name,*args,last_name='unknown',**kwargs):
    print(name)
    print(args)
    print(last_name)
    print(kwargs)

func('abhishek',1,2,3,a=1,b=2)