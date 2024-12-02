from functions import decode_lists
from functions import sort_lists
from functions import compute_distance_between_lists

input_file = "day_1/star_1/input.txt"

right_list, left_list = decode_lists(input_file=input_file)

sorted_right_list, sorted_left_list = sort_lists(right_list=right_list, left_list=left_list)

print("----------LIST----------")
for i in range(len(sorted_left_list)) : 
    print(f"{sorted_left_list[i]} / {sorted_right_list[i]}")
distance = compute_distance_between_lists(sorted_right_list,sorted_left_list)
print("---------RESULT---------")
print(distance)