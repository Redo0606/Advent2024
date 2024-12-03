from functions import extract_numbers_from_brackets
from functions import compute_final_result
from functions import decode_input

# Example usage
text = decode_input(input_file="day_3/input.txt")
numbers_list = extract_numbers_from_brackets(text)
final_result = compute_final_result(numbers_list)
print(f"FINAL RESULT : {final_result}")