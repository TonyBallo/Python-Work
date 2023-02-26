# defining two python arrays of equal length
libraries = ["NumPy", "SciPy", "Pandas", "Matplotlib", "Seaborn"]
completion = [100, 100, 96, 0, 0]

# adding annother entry to each array
libraries.append("scikit-learn")
completion.append(0)

# use zip() to combine two equaly sized arrarys into a two dimensional array of the same size
gradebook = list(zip(libraries, completion))

print("Lesson Completion Rates: ")
print(gradebook)
print("\n")

# adding another entry to the two dimesional grade book array
gradebook.append(("BeautifulSoup", 0))
gradebook.append(("Tensorflow", 0))
print("\n")
print(gradebook)