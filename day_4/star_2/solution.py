from functions import decode_input
from functions import get_sliding_windows
from functions import get_total_count
lines = decode_input(input_file="day_4/star_2/input.txt")

count = get_total_count(lines=lines)

print(f"RESULT : {count}")