# square = (i**2 for i in range(1,11));
# for num in square :
#     print(num)
import time

t1 = time.time()

# List v/s Generator

# l = [i**2 for i in range(100000000)]
g = (i**2 for i in range(100000000))
# for num in g :
#     print(num)
# print(l);
t2 = time.time()
print(t2-t1)