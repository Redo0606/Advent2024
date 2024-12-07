import re 
import itertools
import copy 

def decode_input(input_file):
    """
    Reads the content of the input file and returns the content as a list of strings, one per line.
    """
    try:
        with open(input_file, 'r') as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        raise ValueError(f"File '{input_file}' not found.")
    except Exception as e:
        raise ValueError(f"An error occurred while reading the file: {e}")
    
    
def get_input_lists(input_file) : 
    rule_list = []
    update_list = []
    
    input_lines = decode_input(input_file)
    
    rule_pattern = r"(\d+)\|(\d+)"
    
    for input_line in input_lines : 
        # Using re.match to capture the numbers
        match = re.match(rule_pattern, input_line)

        # If a match is found, extract the two numbers
        if match:
            num1, num2 = match.groups()
            rule_list.append([num1, num2])
        else : 
            numbers = re.findall(r'\d+', input_line)
            if numbers :
                update_list.append(numbers)
                
    return rule_list, update_list

def get_page_order(rules) : 
    order = {}
    for rule in rules : 
        num1 = rule[0]
        num2 = rule[1]
        if num1 not in order.keys() : 
            order[num1] = {'after' : [], 'before' : [num2]}
        if num2 not in order.keys(): 
            order[num2] = {'after' : [num1], 'before' : []}
        if num1 in order.keys() and num2 not in order[num1]['before']: 
            order[num1]['before'].append(num2)
        if num2 in order.keys() and num1 not in order[num2]['after'] : 
            order[num2]['after'].append(num1)
    return order

def check_incorrect_update(update, order) : 
    
    for index in range(len(update) - 1) : 
        num = update[index]
        num_1 = update[index + 1]
        if num in order[num_1]['before'] : 
            return update
        if num_1 in order[num]['after'] : 
            return update
        if num in order[num_1]['after'] and num_1 in order[num]['before'] : 
            pass
        
    return False

def check_correct_update(update, order) : 
    
    for index in range(len(update) - 1) : 
        num = update[index]
        num_1 = update[index + 1]
        if num in order[num_1]['before'] : 
            return False
        if num_1 in order[num]['after'] : 
            return False
        if num in order[num_1]['after'] and num_1 in order[num]['before'] : 
            pass
        
    return update

def reorder_update(order_dict, update):
    def key_function(item):
        position = 0
        for other_item in update:
            if other_item in order_dict[item].get('before', []):
                position -= 1
            if other_item in order_dict[item].get('after', []):
                position += 1
        return position

    return sorted(update, key=key_function)


def get_middle_sum(updates, order) : 
    count = 0
    for update in updates : 
        if check_correct_update(update=update, order=order) == False : 
            reordered_update = reorder_update(update=update, order_dict=order)
            if reordered_update : 
                middle = len(update)//2
                count += int(reordered_update[int(middle)])
    return count

