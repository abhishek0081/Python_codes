x =int(input("Enter The power   :"))
n =int(input("\nEnter The nth values from up to which you want power as given : "))

def func(power,*args):
    if args:
        return  {f"{i} to the power {power} is ": i**power for i in args}        
    else:
        return 'You didn`t passed any args'
# print(type(func(x,n+1)))
n =list(range(1,n+1))
z=func(x,*n)
for key,value in z.items():
    print(f"{key}  :  {value}")
