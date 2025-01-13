# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("PyPoll","Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("PyPoll","analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
vote_count = {}
candidate_names = []
votes = []

# Winning Candidate and Winning Count Tracker
winning_count = 0
winning_candidate = ""

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data, delimiter=",")

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:
        candidate_name = row[2]

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1
        
        # Get the candidate's name from the row
        if candidate_name in vote_count:
            vote_count[candidate_name] += 1
        else:
            vote_count[candidate_name] = 1

# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Total Votes: {total_votes}\n")

    # Write the total vote count to the text file
    txt_file.write("Election Results\n")
    txt_file.write("--------------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("--------------------------------\n")

    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name, votes in vote_count.items():
        vote_percentage = (votes/total_votes) * 100

        # Update the winning candidate if this one has more votes
        if vote_count[candidate_name] > winning_count:
            winning_count = vote_count[candidate_name]
            winning_candidate = candidate_name

        # Print and save each candidate's vote count and percentage
        print(f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n")
        txt_file.write(f"{candidate_name}: {vote_percentage:.3f}% ({votes})\n")

    # Generate and print the winning candidate summary
    print(f"\nWinner: {winning_candidate}")
    print(f"Winning Vote Count: {winning_count}")
    print(f"Winning Percentage: {winning_count/total_votes * 100:.3f}%")

    # Save the winning candidate summary to the text file
    txt_file.write("\n------------------------\n")
    txt_file.write(f"\nWinner: {winning_candidate}")
    txt_file.write(f"\nWinning Vote Count: {winning_count}\n")
    txt_file.write(f"Winning Percentage: {winning_count/total_votes * 100:.3f}%\n")
    txt_file.write("------------------------\n")