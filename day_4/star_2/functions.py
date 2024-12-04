import re


def decode_input(input_file):
    """
    Reads the content of the input file and returns the content as a list of strings, one per line.
    """
    try:
        with open(input_file, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise ValueError(f"File '{input_file}' not found.")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the file: {e}")


def get_sliding_windows(lines):
    """
    Generates 3x3 sliding windows from the input lines.
    """
    windows = []
    for line_index in range(len(lines) - 2):
        for char_index in range(len(lines[line_index]) - 2):
            window = [
                lines[line_index + i][char_index:char_index + 3]
                for i in range(3)
            ]
            windows.append(window)
    return windows


def get_word_count(lines):
    """
    Counts occurrences of the words "MAS" and "SAM" in a list of strings.
    """
    count = 0
    pattern = r"(?=(MAS|SAM))"
    
    for line in lines:
        count += len(re.findall(pattern, line))
    return count


def get_diagonal_count(lines):
    """
    Counts occurrences of the target words in right diagonal lines.
    """
    diagonals = []

    for row_index, line in enumerate(lines):
        for col_index, char in enumerate(line):
            if len(diagonals) <= row_index + col_index:
                diagonals.append('')
            diagonals[row_index + col_index] += char

    return get_word_count(diagonals)


def get_total_count(lines):
    """
    Returns the total count of valid sliding windows that match the target word count criteria.
    """
    count = 0
    windows = get_sliding_windows(lines)

    for window in windows:
        window_count = get_diagonal_count(window)
        
        flipped_window = [line[::-1] for line in window]
        window_count += get_diagonal_count(flipped_window)

        if window_count == 2:
            count += 1

    return count
