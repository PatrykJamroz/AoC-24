def read_input_file(file_path):
    """
    Read input file
    """
    left_list = []
    right_list = []

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            left, right = map(int, line.split())
            left_list.append(int(left))
            right_list.append(int(right))
    
    return left_list, right_list

def calculate_total_distance(left_list, right_list):
    """
    Calculate total distance between left and right list
    """
    left_list.sort()
    right_list.sort()
    total_distance = 0

    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])

    return total_distance

def count_similarity(left_list, right_list):
    """
    Count similarity between left and right list
    """
    similarity = 0

    for i in range(len(left_list)):
        i_count = right_list.count(left_list[i])
        _similiarity = left_list[i] * i_count
        similarity += _similiarity

    return similarity

def main():
    """
    Day 1: Historian Hysteria
    """
    left_list, right_list = read_input_file('input.txt')
    total_distance = calculate_total_distance(left_list, right_list)
    similarity = count_similarity(left_list, right_list)

    print('total distance: ', total_distance, 'similarity: ', similarity)
    return total_distance, similarity

    
if __name__ == "__main__":
    main()