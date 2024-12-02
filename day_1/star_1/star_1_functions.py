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

def sort_lists(right_list, left_list):
    """
    Sorts two lists (`right_list` and `left_list`) based on the elements of `right_list`.
    
    This function sorts both `right_list` and `left_list` such that the order of elements
    in `right_list` is preserved, while the corresponding elements in `left_list` follow the same order.
    
    Args:
        right_list (list): The list to sort by.
        left_list (list): The list whose elements correspond to the sorted elements of `right_list`.
    
    Returns:
        tuple: A tuple containing two lists:
            - right_list: The sorted right_list.
            - left_list: The sorted left_list, corresponding to the sorted `right_list`.
    
    Example:
        right_list, left_list = sort_lists(right_list, left_list)
    """
    right_list_sorted = sorted(right_list)
    left_list_sorted = sorted(left_list)
    return right_list_sorted, left_list_sorted

def compute_distance_between_lists(right_list, left_list):
    """
    Computes the sum of absolute differences between corresponding elements of two lists.
    
    Args:
        right_list (list of str or numbers): The first list of numerical strings or numbers.
        left_list (list of str or numbers): The second list of numerical strings or numbers.
    
    Returns:
        float: The sum of the absolute differences between corresponding elements.
    
    Raises:
        ValueError: If the lists contain non-numeric strings or if their lengths do not match.
    """
    if len(right_list) != len(left_list):
        raise ValueError("The two lists must have the same length.")
    
    difference_list = []
    for i in range(len(right_list)):
        try:
            num1 = float(right_list[i])
            num2 = float(left_list[i])
        except ValueError as e:
            raise ValueError(f"Non-numeric value found: {e}")
        
        difference_list.append(abs(num1 - num2))
    
    return sum(difference_list)