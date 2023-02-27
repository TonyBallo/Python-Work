
numbers = [1, 2, 3, 4, 5, 6]

# map can apply a function to multiple values of a structure
squared_nums = list(map(lambda a:a**2, numbers))

print(squared_nums)


num1 = [1, 2, 3]
num2 = [5, 8, 9]

# it can also do this to multiple value arrays
result = map(lambda a,b:a+b, num1, num2)
print(list(result))



numbers = [234, 3245, 639, 550, 654]

# the filter function takes a function and uses it to filter out an array. 
even_numbers = list(filter(lambda n:n%2 == 0, numbers))

print(even_numbers)