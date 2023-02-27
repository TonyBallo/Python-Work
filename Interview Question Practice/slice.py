# normal slice
numbers = [1, 2 ,8, 4, 9, 12, 15, 73, 23]

# top 3
print("----top 3-----")
print(numbers[0 : 3])
print(numbers[:3])


# bottom 3
print("----bottom 3-----")
print(numbers[-3:])

# printing out a list with a step of 2
print("----with step-----")
print(numbers[0: : 2])


# printing a list in reverse 
print("----reverse a list-----")
print(numbers[::-1])

# editing using slices
numbers[:3] = [-1, -2, -3]
print("edited using slices")
print(numbers)