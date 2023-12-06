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

        $ python3 app_01.py

Attributes:
    FILE_PATH (str): Default file path used when the module is run as a script.
"""


def process_and_sum_numbers(file_path):
    """
    Processes a text file, extracting and summing numbers from each line.

    This function reads a file specified by `file_path` line by line. It replaces
    any spelled-out numbers with digits, then extracts and concatenates the first
    and last digits of each line to form a number. It sums these numbers, skipping
    lines without digits. Errors in file handling are raised.

    Args:
        file_path (str): The path to the text file to be processed.

    Returns:
        int: The sum of numbers formed from the first and last digits of each line.

    Raises:
        FileNotFoundError: If the file at `file_path` does not exist.
        Exception: For any other errors encountered during file processing.
    """
    # Mapping spelled out numbers to their integer equivalents.
    number_map = {
        "oneight": "18",
        "twone": "21",
        "threeight": "38",
        "fiveight": "58",
        "sevenine": "79",
        "eightwo": "82",
        "eighthree": "83",
        "nineight": "98",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    total_sum = 0
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                # Replace spelled out numbers with digits.
                for spelled_out, digit in number_map.items():
                    line = line.replace(spelled_out, digit)
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
    """
    Entry point for processing and summing numbers from a file.

    Calls the `process_and_sum_numbers` function with the provided file path,
    prints the resulting sum, and handles any exceptions that occur during processing.

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
    # Default file path used when the module is run as a script.
    FILE_PATH = "./day_01/data/calibration.txt"
    main(FILE_PATH)
