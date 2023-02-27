"""
equivalent of this

def largest(a, b)):
    if a > b :
        return a
    else:
        return b

"""
larger = lambda a,b: a if a>b else b

print(larger(13, 78))



names = ["Alan", "Gregory", "Zlatan", "Jonas", "Tom", "Augustine"]

names.sort()
print("\n\nNormal sort")
print(names)


names.sort(key = lambda x:len(x))
print("\n\nlambda sort")
print(names[::-1])


quickAdd = lambda a,b : a + b
print(quickAdd(10, 12))
