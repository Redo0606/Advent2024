import re

def decode_input(input_file):
    """
    Reads the content of the input file and returns the content as a list of strings, one per line.
    """
    try:
        with open(input_file, 'r') as file:
            rows = file.readlines()

        rows = [row.strip() for row in rows]
        return rows
    except FileNotFoundError:
        raise ValueError(f"File '{input_file}' not found.")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the file: {e}")


def get_horizontal_lines_count(lines):
    """
    Counts occurrences of the target words in horizontal lines.
    """
    return get_word_count(lines)


def get_vertical_lines_count(lines):
    """
    Counts occurrences of the target words in vertical lines.
    """
    columns = ['' for _ in range(len(lines[0]))]
    for row in lines:
        for i in range(len(row)):
            columns[i] += row[i]
    
    return get_word_count(columns)


def get_right_diagonal_count(lines):
    """
    Counts occurrences of the target words in right diagonal lines.
    """
    
    right_diagonals = []
    for row_index, line in enumerate(lines):
        for col_index, char in enumerate(line):
            if len(right_diagonals) <= row_index + col_index:
                right_diagonals.append('')
            right_diagonals[row_index + col_index] += char
    
    return get_word_count(right_diagonals)


def get_left_diagonal_count(lines):
    """
    Counts occurrences of the target words in left diagonal lines (right diagonals flipped).
    """
    flipped_lines = [line[::-1] for line in lines]
    
    return get_right_diagonal_count(flipped_lines)


def get_word_count(lines):
    """
    Counts occurrences of the words "XMAS" and "SAMX" in a list of strings.
    """
    count = 0
    match_history = []

    pattern = r"(?=(XMAS|SAMX))"

    for line in lines:
        matches = re.findall(pattern, line)
        match_history.append(matches)
        count += len(matches)
    return count
