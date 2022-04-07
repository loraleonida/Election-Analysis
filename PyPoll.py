# The data we need to retrieve:

# The total number of votes cast

# A complete list of candidates who received votes

# The total number of votes each candidate won

# The percentage of votes each candidate won

# The winner of the election based on popular vote



#Add our dependencies.
import csv
import os 

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Declare Candidate Options empty list
candidate_options = []

# Declare Candidate Votes empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0  

# Open the election results and read the file.
with open(file_to_load) as election_data:

    #Read the file object with reader function.
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the csv file.
    for row in file_reader:
        # Add to the total vote count to determine total votes cast.
        total_votes +=1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            # Add candidate name to the list of candidates for a 
            # complete list of candidates who received votes.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count to determine
        # total number of votes per candidate.
        candidate_votes[candidate_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count to the terminal.
    election_results = (
    f"\nElection Results\n"
    f"--------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"--------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate by looping through the counts
    # 1. Loop through the candidate list
    for candidate_name in candidate_votes:

        # 2. Retrieve vote count
        votes = candidate_votes[candidate_name]

        # 3. Calculate the percentage of votes
        vote_percentage = float(votes / total_votes) * 100

        # 4. Print candidate name, vote count, and vote % for each candidate
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # 4. Print out each candidate's name, vote count, and percentage 
        # of votes to the terminal.
        print(candidate_results)

        # Save the candidate results to our text file.
        txt_file.write(candidate_results)


        # Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 2. If true, then set winning_count = votes and winning_percentage = vote %
            winning_count = votes
            winning_percentage = vote_percentage
            # 3. Set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    # 4. Print out the winning candidate summary
    winning_candidate_summary = (
        f"---------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------------------\n")
    
    # Save the winning candidates name to the text file.
    txt_file.write(winning_candidate_summary)

