#itertors are methods that are used to iterate collections like list,tuples etc.
"""
p_n_list = [1,3,5,7,11,13,17,23,29]
pn_iterator = iter(p_n_list)
print(next(pn_iterator))
print(next(pn_iterator))
print("*"*60)
for num in pn_iterator:
    print(num)
"""
#Generators is a function that returns an iterator that produce a sequence of values whenever it is iterated over

"""
def custom_generator(n):
    value=0;
    while value<n:
        yield value
        value +=1

value = custom_generator(10)

print(next(value))
print(next(value))
for num in custom_generator(10):
    print(num)


cubes_generator = (i*i*i for i in range(5))
for num in cubes_generator:
    print(num)
"""

def fibonacci_numbers(nums):
    x,y=0,1
    for _ in range(nums):
        x,y = y, x+y
        yield x

def squares(nums):
    for num in nums:
        yield num**2

for value in fibonacci_numbers(10):
    print(value)
    
print("*"*60)

for value in squares(fibonacci_numbers(10)):
    print(value)

print("*"*60)
print(sum( squares(fibonacci_numbers(10))))


