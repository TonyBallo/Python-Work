"""
You are given a string and need to reverse the characters to put them in another array

"""


word = "This is the best tech interview you have done"


# your code here

reversed_word = str(word[::-1])

print(f"this is the original string \n '{word}' \n this is the reversed string \n '{reversed_word}'")




""" 
now you need to strip the spaces from the string and store them in a list for frequency analysis

"""

# first attampt

"""def removeSpace(word: str):
    filtered_word = []
    for letter in word:
        if letter == " ":
            continue
        else:
            filtered_word.append(letter)

    return filtered_word
    char_set = removeSpace(word)


    print(char_set)
"""

# better way to do it

char_set = list(word.replace(" ", ""))

print (char_set)