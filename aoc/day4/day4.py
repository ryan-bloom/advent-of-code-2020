from aoc.helpers import read_lines
import re


def get_passports(input_path):
    passport_list = []
    passport = ""
    for line in read_lines(input_path):
        if line == "\n":
            passport_list.append(passport)
            passport = ""
        else:
            passport += " " + line.strip()

    # put the last passport in!
    passport_list.append(passport)

    return passport_list


test_passports = get_passports("day4/weak_test.txt")
input_passports = get_passports("day4/weak.txt")
test_strong_valid_passports = get_passports("day4/strong_test_valid.txt")
test_strong_invalid_passports = get_passports("day4/strong_test_invalid.txt")


def is_passport_valid(passport_string: str, strong=False):
    pattern = r"(ecl:)|(pid:)|(gry:)|(eyr:)|(byr:)|(iyr:)|(hcl:)|(hgt:)"
    if strong:
        pattern = r"(ecl:(amb|blu|brn|gry|grn|hzl|oth)\b)|(pid:\d{9}\b)|(eyr:20(2[0-9]|30))|(byr:(19[^01][0-9])|(200[0-2]))|(iyr:(20((1[0-9])|20)))|(hcl:#[0-9a-f]{6})|(hgt:((1[5-9]\dcm)|([5-7]\din)))"
    matches = re.findall(pattern, passport_string)
    return len(matches) == 7


def get_num_valid_passports(passports: list, strong=False):
    return sum(
        1 for passport in passports if is_passport_valid(passport, strong=strong)
    )


assert get_num_valid_passports(test_passports) == 2
assert get_num_valid_passports(test_strong_valid_passports, strong=True) == len(
    test_strong_valid_passports
)
assert get_num_valid_passports(test_strong_invalid_passports, strong=True) == 0

print("valid passports:", get_num_valid_passports(input_passports))
print(
    "valid passports (strong):", get_num_valid_passports(input_passports, strong=True)
)
