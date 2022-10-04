# -*- coding: utf-8 -*-
"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


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


def save_csv(csvpath,qualiyfing_loans):
    """Saves the qualifying loans as a CSV file into the path provided

    Args:
        csvpath - The provided CSV file path for the new file
        qualifying_loans - A list of banks that can satisfy the loan

    Returns:
        writes a CSV file with the list of banks
    """

    header= ["Bank"]
    output_path= csvpath
    #Telling user that the program is creating a CSV file
    print("Writing the data to the CSV file...")
    
    #writing the qualifying loans into a CSV file

    with open (output_path, 'w' ) as csvfile :
        csvwriter=csv.writer(csvfile, delimiter = ",")
        csvwriter.writerow(header)
        for row in qualiyfing_loans:
            csvwriter.writerow(row.values())

