from collections import Counter

def decode_lists(input_file):
    """
    Decodes a file into two separate lists by processing each line of the file.
    
    This function opens a given input file, reads its contents, and splits the content into lines. 
    For each non-empty line, it splits the line into two components (separated by whitespace) and 
    appends the first component to the `right_list` and the second component to the `left_list`. 
    The function assumes that each line contains at least two elements separated by whitespace.

    Args:
        input_file (str): The path to the input file to be processed.

    Returns:
        tuple: A tuple containing two lists:
            - right_list: A list of the first element from each non-empty line.
            - left_list: A list of the second element from each non-empty line.

    Raises:
        FileNotFoundError: If the specified input file does not exist.
        IndexError: If a line in the file does not contain at least two elements.
    
    Example:
        right_list, left_list = decode_lists("data.txt")
        print(right_list)
        print(left_list)
    """
    with open(input_file, 'r') as file:
        content = file.read()
        content_list = content.split("\n")
        right_list = []
        left_list = []
        for content in content_list: 
            if len(content.split()) > 0:
                parts = content.split()
                if len(parts) >= 2:
                    right_list.append(parts[0])
                    left_list.append(parts[1])
                else:
                    raise IndexError(f"Line does not contain two elements: '{content}'")
    return right_list, left_list

def count_occurences(left_list, right_list) : 
    right_occurences_count = Counter(right_list)
    sum = 0
    for number in left_list : 
        if number in right_occurences_count.keys() : 
            sum += int(right_occurences_count[number])*int(number)
    return sum