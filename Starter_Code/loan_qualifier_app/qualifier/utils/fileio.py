# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv
from pathlib import Path


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data


def save_csv(qualiyfing_loans):
    """Saves the qualifying loans as a CSV file in data directory

    Args:
        qualifying_loans - A list of lenders that can satisfy the loan

    Returns:
        writes a CSV file with the list of lenders
    """
    #creating a header for the CSV file
    header= ["Name of Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]

    #output path for the file. 
    output_path= Path("./data/Qualifying_loans.csv")

    #Telling user that the program is creating a CSV file
    print("Writing the data to the CSV file...")
    
    #creating qualifying loans CSV file
    with open (output_path, 'w', newline="" ) as csvfile :
        csvwriter=csv.writer(csvfile, delimiter = ",")
        csvwriter.writerow(header)
        for row in qualiyfing_loans:
            csvwriter.writerow(row)

