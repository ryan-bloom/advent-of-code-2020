from collections import defaultdict
from aoc.helpers import read_file_to_list


def get_joltage_differentials(datapath):
    data = set(map(int, read_file_to_list(datapath)))
    differences = defaultdict(int)
    # account for the final diff
    differences[3] += 1
    current_joltage = 0

    for joltage in data:
        diff = joltage - current_joltage
        assert diff <= 3
        differences[diff] += 1
        current_joltage = joltage

    return differences


test_voltage_diffs = get_joltage_differentials("day10/test.txt")
assert test_voltage_diffs[1] == 22
assert test_voltage_diffs[3] == 10

voltage_diffs = get_joltage_differentials("day10/data.txt")
print(voltage_diffs[1] * voltage_diffs[3])


small_test = sorted([16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4])
small_test.append(small_test[-1] + 3)


# too slow, but gets the actual configurations
# def get_num_joltage_configurations(datapath):
#     data = sorted(list(map(int, read_file_to_list(datapath))))
#     configurations = [[0]]
#     for i, joltage in enumerate(data):
#         for configuration in configurations:
#             # if this number is valid, add it
#             if (joltage > configuration[-1]) and (joltage - configuration[-1] <= 3):
#                 configuration.append(joltage)

#             # if the next number could also work here, slice to the previously added number,
#             # and create a new configuration if it doesn't already exist
#             if i + 1 < len(data):
#                 if data[i + 1] > configuration[-2] and (
#                     data[i + 1] - configuration[-2] <= 3
#                 ):
#                     new_sequence = configuration[:-1]
#                     new_sequence.append(data[i + 1])
#                     if new_sequence not in configurations:
#                         configurations.append(new_sequence)

#     return len(configurations)


def get_num_joltage_configurations(datapath):
    data = [0] + sorted(list(map(int, read_file_to_list(datapath))))

    # "cache"
    combinations_by_index = defaultdict(int)

    def get_num_combinations(from_index):
        if cached := combinations_by_index.get(from_index):
            return cached

        combinations = 0
        for i in range(from_index + 1, len(data)):
            # for every number ahead that is <= 3 away, combinations exist with every other combination of that number
            # recursive calls will be memoized once they start to return (because this is slow af otherwise)
            if data[i] - data[from_index] <= 3:
                combinations += get_num_combinations(i)

        # base case is 1 combo (because there is one extra element at the end of the list)
        if from_index == len(data) - 1:
            return 1

        combinations_by_index[from_index] = combinations
        return combinations

    return get_num_combinations(0)


assert get_num_joltage_configurations("day10/test.txt") == 19208
print("part 2", get_num_joltage_configurations("day10/data.txt"))
