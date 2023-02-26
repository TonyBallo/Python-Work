# defining two python arrays of equal length
libraries = ["NumPy", "SciPy", "Pandas", "Matplotlib", "Seaborn"]
completion = [100, 100, 96, 0, 0]

libraries.append("scikit-learn")
completion.append(0)

gradebook = list(zip(libraries, completion))

print("Lesson Completion Rates: ")
print(gradebook)
print("\n")


gradebook.append(("BeautifulSoup", 0))
gradebook.append(("Tensorflow", 0))
print("\n")
print(gradebook)