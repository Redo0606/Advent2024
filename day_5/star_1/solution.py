from functions import get_input_lists
from functions import get_page_order
from functions import get_middle_sum
rules, updates = get_input_lists(input_file="day_5/star_1/input.txt")

print(rules)
print(updates)

page_order = get_page_order(rules=rules)

print(page_order)


count = get_middle_sum(updates=updates, order=page_order)

print(f"COUNT : {count}")