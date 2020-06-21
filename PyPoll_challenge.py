# Goals for Code
# Retrieve Data
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options
candidate_options = []
#List of counties
county_list = []
# Declare the empty dictionary.
candidate_votes = {}
# Dictionary with votes of every county 
county_votes ={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Largest County Turnout tracker
LCT_name = ""
largestcount = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here. 
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Read and print the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        candidate_name = row[2]
        county_name = row[1]

        #To create list of counties and dictionary
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
             # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
     # Print the final vote count to the terminal.
     election_results = (f"\nElection Results\n"f"-------------------------\n"f"Total Votes: {total_votes:,}\n"f"-------------------------\n \nCounty Votes: \n")
     print(election_results, end="")
     # Save the final vote count to the text file.
     txt_file.write(election_results)

     for county in county_votes:
        # Retrieve vote count and percentage.
        countyvotes = county_votes[county]
        countyvote_percent = float(countyvotes) / float(total_votes) * 100
        county_results = (f"{county}: {countyvote_percent:.1f}% ({countyvotes:,})\n")
        # Print each candidate's voter count and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)
        if (countyvotes > largestcount):
            largestcount = countyvotes
            LCT_name = county
     
     largest_county_turnout = ("\n-------------------------\n"f"Largest County Turnout: {LCT_name}""\n-------------------------\n")  
     print(largest_county_turnout) 
     txt_file.write(largest_county_turnout)
     
     for candidate in candidate_votes:
          # Retrieve vote count and percentage.
          votes = candidate_votes[candidate]
          vote_percentage = float(votes) / float(total_votes) * 100
          candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
          # Print each candidate's voter count and percentage to the terminal.
          print(candidate_results)
          #  Save the candidate results to our text file.
          txt_file.write(candidate_results)
          if (votes > winning_count) and (vote_percentage > winning_percentage):
               # If true then set winning_count = votes and winning_percent = vote_percentage.
               winning_count = votes
               winning_percentage = vote_percentage
               # Set the winning_candidate equal to the candidate's name.
               winning_candidate = candidate  
     # Print the winning candidate's results to the terminal.
     winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
     print(winning_candidate_summary)
     # Save the winning candidate's results to the text file.
     # Save the winning candidate's name to the text file.
     txt_file.write(winning_candidate_summary)
