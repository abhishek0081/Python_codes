# GENERATORS
# genrators are iterators

#iterator, iterable

# l  = [1,4,9,16]
 
# Memory  -------> [--------------------------------------]  #  list case
# Genrator case
# Memory  ----->  # use less memory and use less resource than list case



# create your first generator with generator function

# 1.) Generator Fucntion
# 2.) Generator Comprehension

def nums(n):
    for i in range(2,n+1,2):
        # if i%2 ==0:
        # yield(i);  # use yield keyword  to make generator instead of print function
        yield i;

# print(nums(10));
 
for number in nums(10):
    print(number);



# Memory  ---- list case   -[------------]
# Memory (generator) case ----> genrator only one item at one time less resouce use 
# performance increses
# more efficient
