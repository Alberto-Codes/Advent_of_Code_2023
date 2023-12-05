"""
This module provides functionality for processing text files and summing numbers.

It contains two main functions: `process_and_sum_numbers` and `main`. The former
processes a text file, reading line by line, and sums numbers created by
concatenating the first and last digits of each line. The latter function serves
as an entry point to utilize the `process_and_sum_numbers` function, handling
exceptions and printing the final sum of the numbers. 

The module is designed to be executed as a script with a predefined file path. 
In case of file-related errors or processing issues, appropriate exceptions are 
raised, and error messages are printed.

Example:
    To run the module, execute the script with a Python interpreter:

        $ python3 this_module.py

Attributes:
    FILE_PATH (str): Default file path used when the module is run as a script.
"""


def process_and_sum_numbers(file_path):
    """
    Processes a text file, extracting and summing numbers from each line.

    This function opens a file specified by `file_path` and reads it line by
    line. For each line, it extracts the first and last digits, concatenates
    them into a number, and adds this number to a running total. If a line
    contains no digits, a warning is printed and the line is skipped. Errors
    in file handling (e.g., file not found) are reported and raised.

    Args:
        file_path (str): The path to the text file to be processed.

    Returns:
        int: The sum of concatenated numbers derived from the first and last
             digits of each line in the file.

    Raises:
        FileNotFoundError: If the file at `file_path` does not exist.
        Exception: For any other errors encountered during file processing.
    """
    total_sum = 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                digits = [char for char in line.strip() if char.isdigit()]
                if digits:
                    concatenated_number = digits[0] + digits[-1]
                    total_sum += int(concatenated_number)
                else:
                    print("Warning: Line with no digits found. Skipping line.")
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise
    return total_sum


def main(file_path):
    """Processes and sums numbers from a given file.

    This function reads numbers from a specified file, processes them, and calculates their sum.
    It prints the sum of the concatenated numbers. If an error occurs, it prints an error message.

    Args:
        file_path (str): The path to the file containing numbers to be processed.

    Raises:
        Exception: If an error occurs in the process_and_sum_numbers function.
    """
    try:
        sum_of_numbers = process_and_sum_numbers(file_path)
        print(f"The sum of the concatenated numbers is: {sum_of_numbers}")
    except Exception as e:
        print(f"An error occurred in main: {e}")


if __name__ == "__main__":
    FILE_PATH = "./day_01/data/calibration.txt"
    main(FILE_PATH)
