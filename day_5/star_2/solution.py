from functions import get_input_lists
from functions import get_page_order
from functions import get_middle_sum
import time 

start_time = time.time()

rules, updates = get_input_lists(input_file="day_5/star_2/input.txt")

page_order = get_page_order(rules=rules)

count = get_middle_sum(updates=updates, order=page_order)

end_time = time.time()

elapsed_time = end_time - start_time

print(f"COUNT: {count} - Solution found in {elapsed_time:.2f} seconds.")