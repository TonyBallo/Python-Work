import math
"""
instead of doing: 

numbers = []

for i in range(1,6):

    numbers.append(2**i)

print numbers



we can do it in one line
"""


numbers = [i**2 for i in range(1,6)]
print(numbers)


# you could also include a conditional at the end of the comprehension
# this provides and all in one solution for making new lists

numbers = [49, 36, 64, 81, 25]
rootsOfEvens = [math.sqrt(n) for n in numbers if n % 2 == 0]
print(rootsOfEvens)


# we can also map lists together using comprehensions

team1 = ["Jimmy", "Jake", "Jason"]
team2 = ["Anderson", "Anthony", "Alex"]

mappedTeams = [(x,y) for x in team1 for y in team2]
print(mappedTeams)


# set comprehension

word = "programming"

alphabets = {x for x in word}
print(alphabets)


# dictionary comprehension

numbers = [1, 2 , 3, 4, 5, 6]


"""
instead of doing this----

square_dict = dict()

for num in numbers :
    square_dict[num] = num**2


you can do this
"""

square_dict = {num:num**2 for num in numbers}
print(square_dict)




