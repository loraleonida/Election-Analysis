# The data we need to retrieve:

# The total number of votes cast

# A complete list of candidates who received votes

# The total number of votes each candidate won

# The percentage of votes each candidate won

# The winner of the election based on popular vote



#Add our dependencies.
import csv

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Create a filename variable to a direct or indirect path to the file.
file_to_save = 'Analysis/election_analysis.txt'

# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write Header
    txt_file.write("Counties in the Election\n")

    # Write a line separator
    txt_file.write("--------------------------\n")

    # Write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")
    