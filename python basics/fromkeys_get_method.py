# dictionary
# d = { "name " : " unknown"}
d = dict.fromkeys(['name','age','height'],'unknown')
print(d)


# Get method useful

d={'name': 'abhishek','age':23}
print(d.get('ages'))   # beteer 

if d.get('names'):
    print('present')
else:
    print('not present')

    # If none evaluates false
d2=d
d1 =d.copy()
d.clear()
print(d)
print(d1)
print(d2)
print(d1 == d)
User = {'name':'Abhishek kumar','age':21}
print(User.get('name','not found !'))
def cube_finder(n):
    cubes={}
    for i in range(1,n+1):
        cubes[i] = i**3
    return cubes

print(cube_finder(10))



#Word Counter

def Word_counter(s):
    count ={}
    for char in s:
        count[char]=s.count(char)

    return count

print(Word_counter("Abhishek kumar"))