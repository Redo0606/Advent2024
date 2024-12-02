
def decode_lists(input_file):
    """
    Decodes a file into two separate lists by processing each line of the file.

    This function opens a given input file, reads its contents, and splits the content into lines. 
    For each non-empty line, it splits the line into components (separated by whitespace) and 
    appends them as sublists to a main list, `content_lists`.

    Args:
        input_file (str): The path to the input file to be processed.

    Returns:
        list: A list of sublists, where each sublist represents the split components of a line.

    Raises:
        FileNotFoundError: If the specified input file does not exist.
    """
    with open(input_file, 'r') as file:
        rows = file.read().split("\n")
        content_lists = [row.split() for row in rows if row]
    return content_lists


def is_safe(number_list):
    """
    Determines if a list of numbers satisfies safety conditions based on trends and differences.

    A list is considered safe if:
    - All consecutive differences are between 1 and 3 (inclusive).
    - The list follows a consistent trend (either entirely increasing or entirely decreasing).

    Args:
        number_list (list): A list of numbers to check for safety.

    Returns:
        bool: True if the list is safe, otherwise False.
    """
    trend = None
    for i in range(len(number_list) - 1):
        diff = int(number_list[i+1]) - int(number_list[i])
        if diff > 0:
            if trend == "decreasing":
                return False
            trend = "increasing"
        elif diff < 0:
            if trend == "increasing":
                return False
            trend = "decreasing"

    for i in range(len(number_list) - 1):
        difference = abs(int(number_list[i+1]) - int(number_list[i]))
        if difference > 3 or difference <= 0:
            return False

    return True

def make_combinations(number_list) : 
    combinations = []
    for i in range(len(number_list)) : 
        temp_list = number_list.copy()
        temp_list.pop(i)
        combinations.append(temp_list)
    return combinations

def count_total_safe(input_lists):
    """
    Counts the number of safe lists from a collection of lists.

    Args:
        input_lists (list): A list of lists, where each sublist represents a sequence of numbers.

    Returns:
        int: The total count of safe lists.
    """
    count = 0
    for number_list in input_lists:
        if is_safe(number_list=number_list):
            count += 1
        else : 
            combinations = make_combinations(number_list=number_list)
            for combination in combinations : 
                if is_safe(number_list=combination) : 
                    count +=1
                    break
    return count