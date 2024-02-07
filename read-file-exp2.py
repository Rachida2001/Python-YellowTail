#!/usr/bin/python3
def read_file(cars):
    # Preparing a file
    my_file_pointer = open(cars, 'r')
    # Reading file using readlines() function
    my_data = my_file_pointer.readlines()
    output_list = []
    # stripping "\" from each line
    for line in my_data:
        line_with_no_new_line = line.strip('\n')
        output_list.append(line_with_no_new_line)
    return output_list

# Example usage:
file_contents = read_file('cars.csv')

# Print the contents of the file as a list
print(file_contents)
