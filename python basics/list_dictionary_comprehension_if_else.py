# new_list=[i*2 if(i%2==0)else -i for i in range(1,11)]
# print(new_list)

# square = {f"square of {num} is " : num**2 for num in range(1,11)}
# # print(square)
# for k,v in square.items():
#     print(f"{k}  :  {v} ")


# string = 'Abhishek Kumar'
# word_count ={char : string.count(char) for char in string }
# print(word_count)

odd_even= {i : 'even' if(i%2==0)else 'odd' for i in range(1,11) }
for k,v in odd_even.items():
    print(f"{k}  :  {v} ")
# print(odd_even)