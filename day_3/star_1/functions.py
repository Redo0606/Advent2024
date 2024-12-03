import re

def extract_numbers_from_brackets(text):
    # Regex to match only 'mul[...,...]'
    pattern = r"mul\((\d+),(\d+)\)"
    
    # Find all matches in the input text
    matches = re.findall(pattern, text)
    
    # Convert matched groups to integers and return as a list of lists
    return [[int(num1), int(num2)] for num1, num2 in matches]

def compute_final_result(numbers_list) : 
    sum = 0
    for couple in numbers_list : 
        sum += couple[0]*couple[1]
    return sum

def decode_input(input_file):
        # Open the file in read mode
    with open(input_file, 'r') as file:
        content = file.read()
    return content
