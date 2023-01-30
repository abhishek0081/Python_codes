#iterator vs iterables 

from typing import Iterator
# from map_function import square



numbers = [1,2,3,4,5,6] # tuples ,strings --- iterables
squares =map(lambda a:a%2 ==0,numbers) #iterator

# for i in numbers:
#     print(i)
#step call iter fucntion

# iter(numbers) ------> Iterator
# next(iter(numbers))

number_iter =iter(numbers)
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
print(next(number_iter))
# print(next(number_iter))
print(iter(numbers))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))
print(next(squares))