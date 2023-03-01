languages = [
    "Python"
    "C++"
    "Java"
    "JavaScript"
    "Go"
]


"""
Here is the normal way to do it

found = False

for language in languages :
    if language == "Rust"
        found = true

"""

# Here is the better way to do it in python

for language in languages :
    if language == "Rust":
        print("Item Found")
else:
    print("Item Not Found")