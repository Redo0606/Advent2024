from functions import decode_lists
from functions import count_occurences

input_file = "day_1/star_2/input.txt"

right_list, left_list = decode_lists(input_file=input_file)

count = count_occurences(left_list=left_list, right_list=right_list)
print(count)