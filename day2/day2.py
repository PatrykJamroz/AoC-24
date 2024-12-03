def is_increasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] >= lst[i + 1]:
            return False
    return True

def is_decreasing(lst):
    for i in range(len(lst) - 1):
        if lst[i] <= lst[i + 1]:
            return False
    return True

def check_adjacent_differences(lst):
    for i in range(len(lst) - 1):
        if not (1 <= abs(lst[i] - lst[i + 1]) <= 3):
            return False
    return True

def check_safety(lst):
    if (is_increasing(lst) or is_decreasing(lst)) and check_adjacent_differences(lst):
        return 'safe'
    
    for i in range(len(lst)):
        new_lst = lst[:i] + lst[i+1:]
        if (is_increasing(new_lst) or is_decreasing(new_lst)) and check_adjacent_differences(new_lst):
            return 'safe'
    
    return 'unsafe'

def read_input_file(file_path):
    input_list = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            input_list.append([int(i) for i in line.split()])
    return input_list

def main():
    inputs = read_input_file('input.txt')
    safe_count = 0
    for lst in inputs:
        if check_safety(lst) == 'safe':
            safe_count += 1
    print(safe_count)

if __name__ == "__main__":
    main()