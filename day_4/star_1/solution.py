from functions import get_horizontal_lines_count
from functions import get_vertical_lines_count
from functions import get_right_diagonal_count
from functions import get_left_diagonal_count
from functions import decode_input
lines = decode_input(input_file='day_4/star_1/input.txt')
sum = 0
sum += get_horizontal_lines_count(lines)
sum +=  get_vertical_lines_count(lines)
sum +=  get_right_diagonal_count(lines)
sum +=  get_left_diagonal_count(lines)
print(f"TOTAL COUNT : {sum}")