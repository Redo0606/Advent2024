from functions import decode_input
from functions import extract_numbers_and_instructions_from_brackets
from functions import compute_final_result
input = decode_input(input_file="day_3/star_2/input.txt")

extracts = extract_numbers_and_instructions_from_brackets(text=input)
result = compute_final_result(extracts)
print(f"RESULT : {result}")