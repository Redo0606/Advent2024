from functions import decode_lists
from functions import count_total_safe

input_file = "day_2/star_2/input.txt"
input_lists = decode_lists(input_file=input_file)

result = count_total_safe(input_lists=input_lists)
print(f"TOTAL SAFE NUMBER LISTS : {result}")