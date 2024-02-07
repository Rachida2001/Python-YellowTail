#!/usr/bin/python3
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            # Remove newline characters from each line
            lines = [line.strip() for line in lines]
            return lines
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []

# Test the function with the provided file
filename = input("Enter filename: ")
lines = read_file(filename)
print(lines)
