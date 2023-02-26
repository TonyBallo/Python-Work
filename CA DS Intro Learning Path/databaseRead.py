# this is a boiler plate template for reading a database in python
# this code WILL NOT compile on its own


# import pandas and the database file (usually a csv)
import pandas as pd
import codeacademylib3_seaborn      # this would replaced with the database used


# Load the desired data to a data object

df = pd.read_csv('page_visits.csv') # assuming the .csv file is downloaded to the machine already


# do some optional manipulation of the data


# Display the data

print(df.head()) #this would be the head (first 5 rows) of the data object





